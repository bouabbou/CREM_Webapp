"""
Production settings for CREM_Webapp project.

This file contains production-specific security settings.
Import and override base settings for production deployment.
"""

import os
from pathlib import Path
from decouple import config, Csv
import dj_database_url

# Import base settings
from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default=os.environ.get('SECRET_KEY'))

# Allowed hosts for production
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='labs.ueuromed.org,196.200.182.16', cast=Csv())

# Database configuration for production
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default=os.environ.get('DATABASE_URL')),
        conn_max_age=600,
        ssl_require=True
    )
}

# Security middleware settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_REFERRER_POLICY = 'same-origin'

# HTTPS/SSL settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Email configuration for production
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@labs.ueuromed.org')

# Static files configuration for production
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files configuration
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Logging configuration for production
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'security.log',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': False,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['security_file', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

# CORS settings (if needed)
CORS_ALLOWED_ORIGINS = [
    "https://labs.ueuromed.org",
    "https://www.labs.ueuromed.org",
]

# Content Security Policy (CSP) settings
# Note: This requires django-csp middleware to be installed
# MIDDLEWARE.insert(0, 'csp.middleware.CSPMiddleware')
# CSP_DEFAULT_SRC = ("'self'",)
# CSP_STYLE_SRC = ("'self'", "'unsafe-inline'", "https://fonts.googleapis.com")
# CSP_SCRIPT_SRC = ("'self'",)
# CSP_FONT_SRC = ("'self'", "https://fonts.gstatic.com")
# CSP_IMG_SRC = ("'self'", "data:")

# Rate limiting settings (if using django-ratelimit)
# RATELIMIT_ENABLE = True

# File upload settings
FILE_UPLOAD_MAX_MEMORY_SIZE = 26214400  # 25MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 26214400  # 25MB

# Session settings
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_COOKIE_HTTPONLY = True
SESSION_SAVE_EVERY_REQUEST = False

# CSRF settings
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_AGE = 31449600  # 1 year in seconds
CSRF_USE_SESSIONS = False

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Ensure the logs directory exists
os.makedirs(BASE_DIR / 'logs', exist_ok=True)