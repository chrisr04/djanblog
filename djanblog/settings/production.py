from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['djanbloginvestigation.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd470ateft2iu52',
        'USER': 'rbgillkapnllsn',
        'PASSWORD': '2f55e3a7c92b627aa77e2148bc00653d5e7d4e73d81e4c0d4bf33863e1c04767',
        'HOST': 'ec2-54-83-1-101.compute-1.amazonaws.com',
        'PORT': 5432,
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'djanblog',
    #     'USER':'root',
    #     'PASSWORD':'1083031426Mr)',
    #     'PORT':'3306',
    # }
}

STATIC_ROOT = 'static'