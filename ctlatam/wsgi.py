''' Communities Tech Latam wsgi '''

import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ctlatam.settings')

application = get_wsgi_application()
