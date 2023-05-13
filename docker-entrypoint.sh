#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py collectstatic --noinput

# Start server
echo "Starting server"
gunicorn --env DJANGO_SETTINGS_MODULE=storefront.settings.prod storefront.wsgi --bind 0.0.0.0:8000