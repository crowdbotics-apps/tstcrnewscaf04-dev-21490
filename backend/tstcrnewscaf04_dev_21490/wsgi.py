"""
WSGI config for tstcrnewscaf04_dev_21490 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tstcrnewscaf04_dev_21490.settings')

application = get_wsgi_application()
