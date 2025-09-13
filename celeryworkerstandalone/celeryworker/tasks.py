from celery import shared_task

@shared_task
def task1():
    return True

@shared_task
def task2():
    return True