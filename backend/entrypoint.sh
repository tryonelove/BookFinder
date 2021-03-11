#!/bin/bash
python manage.py db update
python manage.py db upgrade
exec gunicorn --config /app/gunicorn_config.py server.app:app
