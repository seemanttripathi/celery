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