from student_database.settings.base import *  # noqa

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lauder',
        'USER': os.environ.get('DB_USER', ''),
        'HOST': os.environ.get('DB_HOST', ''),
        'PORT': os.environ.get('DB_PORT', ''),
        'PASSWORD': os.environ.get('DB_PASSWORD', ''),
    }
}
