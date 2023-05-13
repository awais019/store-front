#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py collectstatic --noinput
DJANGO_SUPERUSER_USERNAME=testuser \
DJANGO_SUPERUSER_PASSWORD=testpass \
DJANGO_SUPERUSER_EMAIL="admin@admin.com" \
python manage.py createsuperuser --noinput

# Start server
echo "Starting server"
gunicorn --env DJANGO_SETTINGS_MODULE=storefront.settings.prod storefront.wsgi --bind 0.0.0.0:8000