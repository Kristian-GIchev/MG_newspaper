from django.contrib import admin
from django.urls import path, include

from MG_vestnik.myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MG_vestnik.myapp.urls')),
]
