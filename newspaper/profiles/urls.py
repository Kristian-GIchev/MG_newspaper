from django.conf.urls.static import static
from django.urls import path

from newspaper import settings
from newspaper.profiles.views import profile

urlpatterns = [
    path('profile', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
