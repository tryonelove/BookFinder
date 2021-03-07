#!/bin/bash
exec gunicorn --config /app/gunicorn_config.py backend.server.app:app