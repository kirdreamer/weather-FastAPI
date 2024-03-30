FROM python:3.12.2-slim

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN python -m pip install poetry

COPY poetry.lock pyproject.toml /app

RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

COPY weather /app/weather
#TODO add docker-compose for .env

CMD [ "uvicorn", "weather.__main__:app", "--host", "0.0.0.0"]