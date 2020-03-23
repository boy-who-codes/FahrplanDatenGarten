"""
Django settings for FahrplanDatenGarten project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import configparser
import os

import dj_database_url

config = configparser.RawConfigParser()
config.read_file(open('env.cfg', encoding='utf-8'))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get("general", "secret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean('general', 'debug', fallback=True)

ALLOWED_HOSTS = config.get("general", 'allowed_hosts', fallback="*").split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'DBApis',
    'FGRFiller',
    'verspaeti',
    'gtfs',
    'netzkarte',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FahrplanDatenGarten.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['FahrplanDatenGarten/templates/'],
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

WSGI_APPLICATION = 'FahrplanDatenGarten.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(
        config.get(
            'general',
            'database_url',
            fallback="sqlite:///../db.sqlite3"))}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = config.get("general", "time_zone", fallback='Europe/Berlin')

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
STATIC_ROOT = config.get("general", "static_root", fallback=None)

# Added SCSS to Compress
COMPRESS_PRECOMPILERS = [
    ('text/x-scss', 'django_libsass.SassCompiler'),
]
LIBSASS_SOURCE_COMMENTS = False
COMPRESS_ROOT = os.path.join(BASE_DIR, "static")


CACHES = {
    'default': {
        'BACKEND': config.get(
            "caching",
            "backend",
            fallback='django.core.cache.backends.dummy.DummyCache'),
        'LOCATION': config.get(
            "caching",
            "location",
            fallback=""),
    }}


# Celery configuration
# https://docs.celeryproject.org/en/latest/userguide/configuration.html

CELERY_RESULT_BACKEND = config.get(
    'celery',
    'result_backend',
    fallback='redis://localhost/0')

CELERY_BROKER_URL = config.get(
    'celery',
    'broker_url',
    fallback='redis://localhost/0')

CELERY_TASK_SERIALIZER = 'json'

# FahrplanDatenGarten's custom configuration
PERIODIC_IMPORT_TIMETABLES = config.get(
    "periodic", 'timetables', fallback="*,15").split(',')

PERIODIC_IMPORT_JOURNEYS = config.get(
    "periodic", 'timetables', fallback="*,5").split(',')
