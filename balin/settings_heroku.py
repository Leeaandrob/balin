# -*- coding: utf-8 -*-
from settings import *

DEBUG = False

ALLOWED_HOSTS = [
    '*',
]

DEFAULT_FILE_STORAGE = 'balin.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'balin.s3utils.StaticRootS3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('BUCKET_NAME', '')
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Expires': 'Thu, 15 Apr 2010 20:00:00 GMT',
    'Cache-Control': 'max-age=86400',
}

MEDIA_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = 'https://%s.s3.amazonaws.com/static/' % AWS_STORAGE_BUCKET_NAME
