FROM python:3.9 AS base

WORKDIR /code
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "${PATH}:/root/.local/bin"
RUN poetry config virtualenvs.create false

WORKDIR /code/simple-fastapi-app
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install
RUN rm -rf ./*

FROM base
COPY main.py main.py

EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000
