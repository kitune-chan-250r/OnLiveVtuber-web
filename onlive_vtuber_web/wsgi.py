"""
WSGI config for onlive_vtuber_web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlive_vtuber_web.settings')

application = Cling(get_wsgi_application()) #heroku
#application = get_wsgi_application() #local

