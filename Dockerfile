FROM python:3.8.12-slim-buster@sha256:55ef3d2132dec7f372f4d63fbec0027e23388ab072533edbba9ca213a053c9cb AS build
RUN useradd -m developer \
    && mkdir /app \
    && chown -R developer:developer /app \
    && chown -R developer:developer /home/developer/ \
    && mkdir /packages \
    && chown -R developer:developer /packages
USER developer
WORKDIR /app
COPY requirements*.txt ./
RUN pip install --disable-pip-version-check -r requirements.txt --target /packages
COPY api /app/api
COPY common /app/common
COPY gunicorn.conf.py .

FROM gcr.io/distroless/python3@sha256:eb773dd9d39f0becdab47e2ef5f1b10e2988c93a40ac8d32ca593096b409d351
WORKDIR /app
COPY --from=build /app /app
COPY --from=build /packages /packages
ENV PYTHONPATH=/packages
CMD ["/packages/gunicorn/app/wsgiapp.py","api.wsgi:app"]
