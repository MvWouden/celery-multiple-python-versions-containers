# Worker Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root --no-dev --no-interaction

COPY . .

CMD ["poetry", "run", "celery", "-A", "tasks", "worker", "--loglevel=info"]
