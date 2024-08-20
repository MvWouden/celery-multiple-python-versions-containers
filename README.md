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

## Example output

Orchestrator:
```shell
...
orchestration_example-orchestrator-1  | Task triggered with id: a3ef1698-b7aa-44d5-9d0e-542ac871526f
orchestration_example-orchestrator-1  | Task result: 30
```

Worker:
```shell
...
orchestration_example-worker-1  | [2024-08-20 20:20:48,874: INFO/MainProcess] celery@a824cc9bd983 ready.
orchestration_example-worker-1  | [2024-08-20 20:20:48,875: INFO/MainProcess] Task tasks.add[a3ef1698-b7aa-44d5-9d0e-542ac871526f] received
orchestration_example-worker-1  | [2024-08-20 20:20:48,981: INFO/ForkPoolWorker-16] Task tasks.add[a3ef1698-b7aa-44d5-9d0e-542ac871526f] succeeded in 0.00422586500098987s: 30
```
