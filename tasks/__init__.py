from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')

app.conf.CELERY_TASK_SERIALIZER = 'json'