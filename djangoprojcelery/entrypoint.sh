#!/bin/ash

echo "Appliy database migrations"
python manage.py migrate

exec "$@"