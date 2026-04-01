#!/usr/bin/env bash
set -o errexit
pip install -r chaiheadq/requirements.txt
python chaiheadq/manage.py collectstatic --noinput
python chaiheadq/manage.py migrate
