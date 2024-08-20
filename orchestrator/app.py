from celery import Celery


app = Celery('orchestrator', broker='amqp://user:password@rabbitmq:5672//', backend='redis://redis:6379/0')


# Define Celery task signature
def trigger_task():
    return app.send_task('tasks.add', args=(10, 20))


if __name__ == "__main__":
    # Trigger the task and wait for the result
    result = trigger_task()
    print(f"Task triggered with id: {result.id}")
    # Wait for the result to be ready
    result_value = result.get(timeout=10)
    print(f"Task result: {result_value}")
