pip freeze > requirements.txt
django-admin startproject djangoprojcelery
conda create -n celery python=3.12 
conda activate celery 
pip install django   
pip install celery   
pip install redis
chmod +x ./entrypoint.sh 

docker-compose up -d --build
docker exec -it django /bin/sh
/usr/src/app # ./manage.py startapp celeryworker
./manage.py shell

from celeryworker.tasks import sharedtask
sharedtask.delay()

from celeryworker.tasks import task1, task2
task1.delay()
task2.delay()

from celeryworker.tasks import tp1, tp2, tp3, tp4
tp1.deply()
tp1.deply()
tp1.deply()
tp1.deply()
tp1.deply()
tp2.delay()
tp2.delay()
tp3.delay()
tp3.delay()
tp3.delay()
tp3.delay()
tp3.delay()
tp2.delay()
tp1.deply()
tp1.deply()
tp1.deply()
tp2.delay()
tp4.delay()
tp3.delay()
tp4.delay()
tp2.delay()
tp4.delay()
tp4.delay()

from celery import group
from celeryworker.tasks import tp1, tp2, tp3, tp4
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()