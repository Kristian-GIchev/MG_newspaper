from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('newspaper.article_management.urls')),
    path('', include('newspaper.public.urls')),
    path('', include('newspaper.profiles.urls')),
    path('', include('newspaper.mg_auth.urls')),
]
