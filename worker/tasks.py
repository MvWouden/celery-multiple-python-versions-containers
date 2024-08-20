from celery import Celery


app = Celery('tasks', broker='amqp://user:password@rabbitmq:5672//', backend='redis://redis:6379/0')


@app.task
def add(x, y):
    return x + y
