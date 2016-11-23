"""
Django settings for inventory_MIS project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import socket

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = 'rglzsfv3*xljon1*_38h-92a2btokfc+@v@m-mq!yjpftx_)!!'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inventory_module',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Inventory_MIS.urls'

# Add static folder to STATIC_DIRS
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# Add templates to DIRS
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Inventory_MIS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Inventory_DB',
        'USER': 'root',
        'PASSWORD': '123..',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


"""
Static files (CSS, JavaScript, Images)
https://docs.djangoproject.com/en/1.8/howto/static-files/
"""
STATIC_URL = '/static/'
LOGIN_URL = '/inventory_module/accounts/'
LOGIN_REDIRECT_URL = '/inventory_module/home/'

# Logging setting
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        #'require_debug_false': {
        #    '()': 'django.utils.log.RequireDebugFalse',
        #},
        #'require_debug_true': {
        #    '()': 'django.utils.log.RequireDebugTrue',
        #},
    },
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'development_logfile': {
            'level': 'DEBUG',
           # 'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'logs/django_dev.log',
            'formatter': 'verbose'
        },
        'production_logfile': {
            'level': 'DEBUG',
           # 'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'logs/django_production.log',
            'formatter': 'verbose'
        },
        'dba_logfile': {
            'level': 'DEBUG',
            #'filters': ['require_debug_false', 'require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'logs/django_dba.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'production_logfile', 'development_logfile'],
        },
        'django.db.backends': {
            'handlers': ['console', 'dba_logfile'],
        },
        'django': {
            'handlers': ['console', 'development_logfile', 'production_logfile'],
        },
        'myapp': {
            'handlers': ['console', 'development_logfile', 'production_logfile'],
        }

    }
}