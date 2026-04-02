#!/usr/bin/env bash
set -o errexit
cd chaiheadq
pip install -r requirements.txt
python manage.py migrate --run-syncdb
