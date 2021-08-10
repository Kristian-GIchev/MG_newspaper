from django.contrib import admin
from django.urls import path, include

from MG_vestnik.public.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MG_vestnik.article_management.urls')),
    path('', include('MG_vestnik.public.urls')),
    path('', include('MG_vestnik.profiles.urls')),
    path('', include('MG_vestnik.mg_auth.urls')),
]
