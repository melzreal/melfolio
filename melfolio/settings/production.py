from .base import *
from __future__ import absolute_import, unicode_literals
import os
import dj_database_url

env = os.environ.copy()

DEBUG = False
SECRET_KEY = env['SECRET_KEY']
DATABASES['default'] = dj_database_url.config()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']

try:
    from .local import *
except ImportError:
    pass
