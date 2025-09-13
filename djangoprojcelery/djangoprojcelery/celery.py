import os
from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoprojcelery.settings')

app = Celery('djangoprojcelery')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.task_routes = {
#     'celeryworker.tasks.*': {'queue': 'queue1'},
#     'celeryworker.tasks.task2': {'queue': 'queue2'},
# }
app.conf.broker_transport_options = {
    'priority_steps': list(range(10)),
    'queue_order_strategy': 'priority',
    'separator': ':',
}
# Auto-discover tasks from all installed Django apps
app.autodiscover_tasks()
