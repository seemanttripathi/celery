pip freeze > requirements.txt
django-admin startproject djangoprojcelery
conda create -n celery python=3.12 
conda activate celery 
pip install django   
pip install celery   
pip install redis
chmod +x ./entrypoint.sh 

docker-compose up -d --build