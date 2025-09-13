import os
from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoprojcelery.settings')

app = Celery('djangoprojcelery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.task_routes = {
    'celeryworker.tasks.*': {'queue': 'queue1'},
    'celeryworker.tasks.task2': {'queue': 'queue2'},
}
# Auto-discover tasks from all installed Django apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')