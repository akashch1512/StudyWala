# api/index.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudyWala.settings")
app = get_wsgi_application()
