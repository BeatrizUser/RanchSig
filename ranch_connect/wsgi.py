"""
WSGI config for ranch_connect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ranch_connect.settings')

application = get_wsgi_application()

