#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py collectstatic --noinput
DJANGO_SUPERUSER_USERNAME=awais \
DJANGO_SUPERUSER_PASSWORD=awais@20 \
DJANGO_SUPERUSER_EMAIL="awais@awais.com" \
python manage.py createsuperuser --noinput
python manage.py seed_db

# Start server
echo "Starting server"
gunicorn --env DJANGO_SETTINGS_MODULE=storefront.settings.prod storefront.wsgi --bind 0.0.0.0:8000