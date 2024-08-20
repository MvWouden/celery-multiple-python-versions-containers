# celery-multiple-python-versions-containers

This is a simple example to demonstrate how to orchestrate Celery tasks across different Python versions using Docker Compose and Poetry.

## Components

- **Orchestrator**: Python 3.12 application triggering the Celery task.
- **Worker**: Python 3.9 application processing the Celery task.
- **RabbitMQ**: Used as the message broker.
- **Redis**: Used as the result backend.

## Running the Project

1. Install [Docker (Compose)](https://www.docker.com/).
2. Clone this repository.
3. Navigate to the project directory and run `docker compose up --build`.
4. The orchestrator will trigger a task that the worker will process, and the result will be printed in the orchestrator's output.
