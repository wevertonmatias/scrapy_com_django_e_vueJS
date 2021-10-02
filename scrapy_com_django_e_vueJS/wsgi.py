"""
WSGI config for scrapy_com_django_e_vueJS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapy_com_django_e_vueJS.settings')

application = get_wsgi_application()
