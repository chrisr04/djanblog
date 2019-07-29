from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['djanbloginvestigation.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'djanblog.sqlite3',
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