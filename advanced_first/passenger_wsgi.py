import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/home/t/taras54321/taras54321.beget.tech/advanced_first')
sys.path.insert(1, '/home/t/taras54321/taras54321.beget.tech/djangoenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'advanced_first.settings'

application = get_wsgi_application()
