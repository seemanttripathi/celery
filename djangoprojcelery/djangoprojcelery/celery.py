import os
from celery import Celery 
from kombu import Exchange, Queue
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoprojcelery.settings')

app = Celery('djangoprojcelery')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
          queue_arguments={'x-max-priority': 10}),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1


@app.task(queue='tasks')
def t1():
    time.sleep(3)
    return True

@app.task(queue='tasks')
def t2():
    time.sleep(3)
    return True

@app.task(queue='tasks')
def t3():
    time.sleep(3)
    return True

# app.conf.task_routes = {
#     'celeryworker.tasks.*': {'queue': 'queue1'},
#     'celeryworker.tasks.task2': {'queue': 'queue2'},
# }
# app.conf.broker_transport_options = {
#     'priority_steps': list(range(10)),
#     'queue_order_strategy': 'priority',
#     'separator': ':',
# }
# app.conf.task_default_rate_limit = '2/m'
# Auto-discover tasks from all installed Django apps
app.autodiscover_tasks()
