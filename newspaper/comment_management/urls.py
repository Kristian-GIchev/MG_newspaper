from django.conf.urls.static import static
from django.urls import path

from newspaper import settings
from newspaper.comment_management.views import create_comment, edit_comment, delete_comment, \
    like_comment, view_my_comments

urlpatterns = [
    path('create-comment/<int:article_pk>', create_comment, name='create_comment'),
    path('view-my-comments/', view_my_comments, name='view_my_comments'),
    path('edit-comment/<int:pk>', edit_comment, name='edit_comment'),
    path('delete-comment/<int:pk>', delete_comment, name='delete_comment'),
    path('like-comment/<int:pk>', like_comment, name='like_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
