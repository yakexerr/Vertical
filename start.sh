python manage.py migrate
gunicorn --chdir /code vertical_project.wsgi:application