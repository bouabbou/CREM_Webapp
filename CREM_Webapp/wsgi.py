"""
WSGI config for CREM_Webapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CREM_Webapp.settings")

application = get_wsgi_application()

# Add your project directory to the sys.path
sys.path.append('/home/user/CREM_Webapp')
sys.path.append('/home/user/CREM_Webapp/CREM_Webapp')
