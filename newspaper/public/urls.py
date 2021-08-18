from django.conf.urls.static import static
from django.urls import path

from newspaper import settings
from newspaper.public.views import home, about_us, news, sports, activities, projects, internships, view_article

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('news/', news, name='news'),
    path('sports/', sports, name='sports'),
    path('activities/', activities, name='activities'),
    path('projects/', projects, name='projects'),
    path('internships/', internships, name='internships'),
    path('view-article/<int:pk>', view_article, name='view_article'),

    # path('web-dev/', web_dev, name='web_dev'),
    # path('literature/', literature, name='literature'),
    # path('cinema/', cinema, name='cinema'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
