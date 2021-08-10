from django.conf.urls.static import static
from django.urls import path

from MG_vestnik import settings
from MG_vestnik.user_auth.views import u_logout, u_register, u_login

urlpatterns = [
    path('login/', u_login, name='login'),
    path('register/', u_register, name='register'),
    path('logout/', u_logout, name='logout'),
    path('profile', u_login, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
