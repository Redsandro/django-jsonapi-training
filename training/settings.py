"""
Django settings for training project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from distutils.util import strtobool

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'c3pz+#@g%crl=bihc347a5)+l@cp==cs=d!3@p7*+_3!fd!yzu')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = strtobool(os.environ.get('DJANGO_DEBUG', 'true'))
SQLSERVER = strtobool(os.environ.get('DJANGO_SQLSERVER', 'false'))

ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'debug_toolbar',
    'corsheaders',
    'oauth2_provider',
    'django_filters',
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'training.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'training.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

if SQLSERVER:
    # Use the following if testing with MS SQL:
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': os.environ['DJANGO_SQLSERVER_DB'],
            'USER': os.environ['DJANGO_SQLSERVER_USER'],
            'PASSWORD': os.environ['DJANGO_SQLSERVER_PASS'],
            'HOST': os.environ['DJANGO_SQLSERVER_HOST'],
            'PORT': '1433',
            'OPTIONS': {
                # 'driver': 'ODBC Driver 13 for SQL Server', # 17 blows up on MacOS??
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'OPTIONS': {
                'timeout': 20,
            }
        }
    }



# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# DRF and DJA settings
REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiPageNumberPagination',
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework_json_api.pagination.JsonApiLimitOffsetPagination',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_json_api.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',  # application/vnd.api+json
        'rest_framework.renderers.BrowsableAPIRenderer',  # text/html: ?format=api
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework_json_api.filters.QueryParameterValidationFilter',  # for query parameter validation
        'rest_framework_json_api.filters.OrderingFilter',  # for sort
        'rest_framework_json_api.django_filters.DjangoFilterBackend',    # for `filter[field]` filtering
        'rest_framework.filters.SearchFilter',    # for keyword filtering across multiple fields
    ),
    'SEARCH_PARAM': 'filter[search]',
    'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
    'TEST_REQUEST_DEFAULT_FORMAT': 'vnd.api+json',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework_json_api.renderers.JSONRenderer',
    ),
}

JSON_API_FORMAT_TYPES = 'underscore'
# JSON_API_FORMAT_FIELD_NAMES = 'camelize'
JSON_API_PLURALIZE_TYPES = True

# django-oauth-toolkit settings
CORS_ORIGIN_ALLOW_ALL = True

OAUTH2_PROVIDER = {
    # here's where we add the external introspection endpoint:
    'RESOURCE_SERVER_INTROSPECTION_URL': os.environ.get('OAUTH2_SERVER','https://oauth-test.cc.columbia.edu')
                                            + '/as/introspect.oauth2',
    'RESOURCE_SERVER_INTROSPECTION_CREDENTIALS': (
        os.environ.get('RESOURCE_SERVER_ID','demo_resource_server'),
        os.environ.get('RESOURCE_SERVER_SECRET','wL0pgS5RcNOgdOSSmejzZNA605d3MtkoXMVSDaJxmaTU70XnYQPOabBAYtfkWXay')
    ),
}

# debug logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(asctime)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'oauth2_provider': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'myapp': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'cuit_enterprise_scope_shim': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
    }
}
