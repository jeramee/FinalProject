# DjangoTest3/urls.py
import os
import logging
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (
    base_view, index_view, post_view, jupyterlite_view,
    register_view, login_view, create_view, logout_view
)


# Set up logging
LOGGING_DIR = os.path.join(settings.BASE_DIR, 'logs')
os.makedirs(LOGGING_DIR, exist_ok=True)

LOGGING_CONFIG = None
LOGLEVEL = os.environ.get('LOGLEVEL', 'info').upper()
LOG_FILE = os.path.join(LOGGING_DIR, 'urls.log')

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
    path('base/', base_view, name='base'),
    path('', index_view, name='index'),
    path('post/', post_view, name='post'),
    path('jupyter/', jupyterlite_view, name='jupyter'),  # Update this line    path('page5/', page5, name='page5'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Fix the import path for 'blog.urls'
    path('create/', create_view, name='blog_create'),  # Add this line for create_view

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

logger.info('DjangoTest3 URL patterns loaded successfully.')
