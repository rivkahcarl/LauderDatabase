from student_database.settings.base import *  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qb7yh%ince741dkvst4)j0-&7(0_pa_(o*@rh7qfokz3l@2qv0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lauder',
        'USER': 'lauder_test_user',
        'HOST': 'localhost',
        'PASSWORD': 'lauder_pass',
    }
}
