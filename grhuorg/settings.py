"""
Django settings for grhuorg project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

from secret_settings import DATABASE, S_KEY

SECRET_KEY = S_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.grhu.org',
    '.grhu.ca',
]


# Application definition

INSTALLED_APPS = (
    #'django_admin_bootstrapped.bootstrap3',
    #'django_admin_bootstrapped',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'about',
    'blog',
    'event',
    'news',
    'photo_album',
    'press',
    'project',
    'south',
    'sorl.thumbnail',
    'lib',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'grhuorg.urls'

WSGI_APPLICATION = 'grhuorg.wsgi.application'

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 600

SITE_ID=1

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = DATABASE

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),]

STATIC_URL = 'http://grhu.org/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static")
)
MEDIA_URL = 'http://grhu.org/media/'
MEDIA_ROOT = os.path.join(
    os.path.join(BASE_DIR, "media"),
)

# This forces or relaxes auto-now-add and auto-now in models:
FORCE_AUTO_NOW=False

#Template Context Processor allows page to refer to own url.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)

#Caching Information:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

"""
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/home/pbulsink/webapps/grhuorg/django_cache', 
        'TIMEOUT': 600,
    }
}
"""
