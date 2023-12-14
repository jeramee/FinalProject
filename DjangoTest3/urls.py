from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (
    base_view, index_view, post, jupyter, page3, page4, page5,
    register_view, login_view, create_view, logout_view
)
from blog.views import notebook_view

urlpatterns = [
    path('base/', base_view, name='base'),
    path('', index_view, name='index'),
    path('post/', post, name='post'),
    path('jupyter/', jupyter, name='jupyter'),
    path('page3/', page3, name='page3'),
    path('page4/', page4, name='page4'),
    path('page5/', page5, name='page5'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Fix the import path for 'blog.urls'
    path('create/', create_view, name='blog_create'),  # Add this line for create_view
    path('notebook/', notebook_view, name='notebook_view'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
