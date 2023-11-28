#!/bin/sh

python3 manage.py migrate
python3 manage.py collectstatic
uwsgi --enable-threads --http :8000 --wsgi-file /opt/taxation/core/wsgi.py
