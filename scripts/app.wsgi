import sys 
from . import settings
sys.path.insert(0, f"/var/www/{settings.APP_NAME}")
from .app import app 