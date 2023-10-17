"""
WSGI config for projet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# DOTENV
load_dotenv(BASE_DIR.parent / 'dotenv_files' / '.env', override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')

application = get_wsgi_application()
