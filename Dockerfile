FROM python:3.9.2-slim-buster@sha256:721de1d0aea3331da282531b8b9e428d552b89bd6fd0d0c14e634deaddc241fc as build
RUN groupadd auth0 && useradd -m developer -g auth0
USER developer
WORKDIR /home/developer
COPY ./requirements.txt ./app/requirements.txt
RUN pip install --disable-pip-version-check -r ./app/requirements.txt --target ./packages
COPY ./api ./app/api
COPY ./common ./app/common
COPY ./gunicorn.conf.py ./app

FROM gcr.io/distroless/python3@sha256:eb773dd9d39f0becdab47e2ef5f1b10e2988c93a40ac8d32ca593096b409d351
COPY --from=build /home/developer/app /app
COPY --from=build /home/developer/packages /packages
USER 1000
EXPOSE 6060
ENV PYTHONPATH="/packages"
WORKDIR /app
CMD ["/packages/gunicorn/app/wsgiapp.py","api.wsgi:app"]
