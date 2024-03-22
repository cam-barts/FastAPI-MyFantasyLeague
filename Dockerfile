FROM python:3.11 as requirements-stage

WORKDIR /tmp

RUN pip install pipenv

COPY Pipfile Pipfile.lock /tmp/

RUN pipenv requirements > /tmp/requirements.txt

FROM python:3.11

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt \
    && adduser --system --no-create-home fastapi \
    && chown -R fastapi /code

USER fastapi

COPY --chown=101:101 ./src /code/src

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

CMD ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
