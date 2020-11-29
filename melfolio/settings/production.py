import os
import dj_database_url

from .base import *

DEBUG = False

env = os.environ.copy()

ALLOWED_HOSTS = ['*']

if 'SECRET_KEY' in env:
    SECRET_KEY = env['SECRET_KEY']

if 'ALLOWED_HOSTS' in env:
    ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

if 'DATABASE_URL' in os.environ:
    DATABASES = {
      'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mel_newfolio_db',
            'CONN_MAX_AGE': 600,
        }
    }


try:
    from .local import *
except ImportError:
    pass
