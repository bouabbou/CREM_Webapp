STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'labscrem@gmail.com'
# EMAIL_HOST_PASSWORD = 'qciw olhf jiwy oiwz'
EMAIL_HOST_PASSWORD ='bmir xvwm pajf ufap'