from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('management/', include('newspaper.article_management.urls')),
    path('', include('newspaper.public.urls')),
    path('profiles/', include('newspaper.profiles.urls')),
    path('auth/', include('newspaper.mg_auth.urls')),
]
