#!/usr/bin/env bash

echo "Building project packages..."
pip install -r requirements.txt

echo "Migrating Database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting the application..."
gunicorn a2svhackathon.wsgi:application --bind 0.0.0.0:8000
