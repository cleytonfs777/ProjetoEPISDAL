release: python manage.py migrate && python manage.py createadmin
web: gunicorn myproject.wsgi:application --bind 0.0.0.0:$PORT
