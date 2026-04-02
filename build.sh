#!/usr/bin/env bash
set -o errexit
cd chaiheadq
pip install -r requirements.txt
python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate admin
python manage.py migrate sessions
python manage.py migrate tweet
