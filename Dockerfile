FROM python:3.8.12-slim-buster@sha256:55ef3d2132dec7f372f4d63fbec0027e23388ab072533edbba9ca213a053c9cb AS build
RUN groupadd auth0 && useradd -m developer -g auth0
USER developer
WORKDIR /home/developer/app
COPY requirements*.txt ./
RUN pip install --disable-pip-version-check -r requirements.txt --target /home/developer/packages
COPY api ./api
COPY common ./common
COPY gunicorn.conf.py .

FROM gcr.io/distroless/python3@sha256:eb773dd9d39f0becdab47e2ef5f1b10e2988c93a40ac8d32ca593096b409d351
WORKDIR /app
COPY --from=build /home/developer/app /app
COPY --from=build /home/developer/packages /packages
USER 1000
ENV PYTHONPATH=/packages
CMD ["/packages/gunicorn/app/wsgiapp.py","api.wsgi:app"]
