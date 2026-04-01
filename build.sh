#!/usr/bin/env bash
set -o errexit
pip install -r chaiheadq/requirements.txt
cd chaiheadq
python manage.py collectstatic --noinput
python manage.py migrate
