#!/usr/bin/env bash

set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
mkdir gallery_mate/media
chmod -R 775 gallery_mate/media
