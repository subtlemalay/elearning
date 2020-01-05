"""
Django settings for myelearning project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from decouple import config
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR,'templates/calendar')
FRONTEND_DIR = os.path.join(BASE_DIR, 'vuejs')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'courses',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.admindocs',
    'students',
    'agenda',
    'blog',
    'embed_video',
    'rest_framework',
    'storages',
    'widget_tweaks',
    'webpack_loader',
    'corsheaders',
    'taggit',
    'taggit_serializer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'students.middleware.SessionTimeoutMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
]

# if DEBUG == False:
    # MIDDLEWARE += ('courses.middleware.SubdomainCourseMiddleware')


ROOT_URLCONF = 'myelearning.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'myelearning.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not DEBUG:
    STATICFILES_DIRS = (
        os.path.join(FRONTEND_DIR, 'dist'),
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

WEBPACK_LOADER = {
    'DEFAULT' : {
        'CACHE': DEBUG,
        'BUNDLE_DIR_NAME': '/bundles/',
        'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json')
    }
}

if not DEBUG:
    WEBPACK_LOADER['DEFAULT'].update({
        'BUNDLE_DIR_NAME': '/dist/',
        'STATS_FILE': os.path.join(FRONTEND_DIR, 'webpack-stats.json')
    })

# Custom auth

AUTH_USER_MODEL = 'students.User'
LOGIN_REDIRECT_URL = reverse_lazy('classroom')
LOGIN_URL = reverse_lazy('login')
LOGOOUT_URL = reverse_lazy('logout')
LOGOUT_REDIRECT_URL = reverse_lazy('course_list')


# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 60 * 15  # 15 minutes
# CACHE_MIDDLEWARE_KEY_PREFIX = 'myelearning'

# DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer',
    )
}

# Mailer
DEFAULT_FROM_EMAIL = config('ADMIN_EMAIL')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Session
SESSION_EXPIRE_SECONDS = 18000  # 5 hours
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True

DEVELOPER_KEY = config('DEVELOPER_API_KEY')

# corsheaders
CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'https://myelearning.herokuapp.com',
    'http://localhost:8080',
    'http://127.0.0.1:8080',
)

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'DELETE',
)
