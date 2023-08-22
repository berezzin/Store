"""
WSGI config for store project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from store.settings import MEDIA_ROOT

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

application = get_wsgi_application()

application = WhiteNoise(application=application, root='/staticfiles')
