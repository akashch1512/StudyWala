import os
import sys

# Add root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StduyWala.settings")

# Import WSGI application
from django.core.wsgi import get_wsgi_application

app = get_wsgi_application() 
