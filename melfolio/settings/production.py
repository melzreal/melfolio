from .base import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

BASE_URL = os.environ.get('BASE_URL')
LIVE_URL = os.environ.get('LIVE_URL')
ALLOWED_HOSTS = [BASE_URL, LIVE_URL]

try:
    from .local import *
except ImportError:
    pass