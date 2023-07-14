"""
WSGI config for ranch_connect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Adicione o diretório raiz do projeto ao sys.path
path = '/home/btrz92/RanchSig'
if path not in sys.path:
    sys.path.append(path)

# Defina a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ranch_connect.settings')

# Obtenha a aplicação WSGI do Django
application = get_wsgi_application()
