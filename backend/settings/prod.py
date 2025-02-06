from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'https://taximanager-backend-1060073980134.us-central1.run.app',
    'taximanager-backend-1060073980134.us-central1.run.app',
    'https://frontend-159812486596.us-central1.run.app',
    'frontend-159812486596.us-central1.run.app',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': f'/cloudsql/{env("CLOUD_SQL_CONNECTION_NAME")}',
        'PORT': '',
    }
}

CSRF_TRUSTED_ORIGINS = [
    'https://taximanager-backend-1060073980134.us-central1.run.app',
    'https://frontend-159812486596.us-central1.run.app'
]