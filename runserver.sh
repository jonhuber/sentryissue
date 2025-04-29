set -eux

PYTHONPATH=./src ./venv/bin/gunicorn -k gevent -c src/simple/gunicorn.conf.py simple.wsgi:application
