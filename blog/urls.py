# blog/urls.py
import os
import logging
from django.urls import path
from .views import index_view, create_view, detail_view, post_view

# Set up logging
LOGGING_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(LOGGING_DIR, exist_ok=True)

LOGGING_CONFIG = None
LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()
LOG_FILE = os.path.join(LOGGING_DIR, 'blog_urls.log')

logging.basicConfig(
    level=LOGLEVEL,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ]
)

logger = logging.getLogger(__name__)

urlpatterns = [
    path('', index_view, name='blog_index'),
    path('create/', create_view, name='blog_create'),
    path('<int:pk>/', detail_view, name='blog_detail'),
    path('post/', post_view, name='blog_post'),
    # Add more paths for other views as needed
]

logger.info('Blog URLs loaded successfully.')
