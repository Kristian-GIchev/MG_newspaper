from django.conf.urls.static import static
from django.urls import path, include

from MG_vestnik import settings
from MG_vestnik.newspaper.views import web_dev, literature, cinema, view_my_articles, create_article, edit_article, \
    delete_article, home, about_us, news, sports, activities, school_projects, international_internships, \
    view_article

urlpatterns = [
    path('', home, name='home'),
    path('about-us/', about_us, name='about_us'),
    path('news/', news, name='news'),
    path('sports/', sports, name='sports'),
    path('activities/', activities, name='activities'),
    path('school-projects/', school_projects, name='school_projects'),
    path('international_internships/', international_internships, name='international_internships'),
    # path('web-dev/', web_dev, name='web_dev'),
    # path('literature/', literature, name='literature'),
    # path('cinema/', cinema, name='cinema'),
    path('create-article/', create_article, name='create_article'),
    path('view-my-articles/', view_my_articles, name='view_my_articles'),
    path('edit-article/<int:pk>', edit_article, name='edit_article'),
    path('delete-article/<int:pk>', delete_article, name='delete_article'),
    path('view-article/<int:pk>', view_article, name='view_article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
