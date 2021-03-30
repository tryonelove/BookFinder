#!/bin/bash
python manage.py db migrate
python manage.py db upgrade
exec gunicorn --config /app/gunicorn_config.py server.app:app
