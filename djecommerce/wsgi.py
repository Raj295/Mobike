import os

from django.core.wsgi import get_wsgi_application
djecomme
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rce.settings')

application = get_wsgi_application()
