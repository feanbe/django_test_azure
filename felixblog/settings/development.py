from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ['DBNAME'],
       'USER': os.environ['DBUSER'],
       'PASSWORD': os.environ['DBPASS'],
       'HOST': os.environ['DBHOST'],
       'PORT': os.environ['DB_PORT'],
   }
}