from django.conf.urls.static import static
from django.urls import path

from newspaper import settings
from newspaper.mg_auth.views import sign_out, u_register, sign_in


urlpatterns = [
    path('sign-in/', sign_in, name='sign-in'),
    path('register/', u_register, name='register'),
    path('sign-out/', sign_out, name='sign-out'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
