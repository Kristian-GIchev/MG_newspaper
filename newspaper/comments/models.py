from django.contrib.auth import get_user_model
from django.db import models

from newspaper.article_management.models import Article
# from newspaper.public.models import Like

UserModel = get_user_model()


class Comment(models.Model):
    content = models.TextField(
        max_length=500,
    )
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, blank=True, null=True)
    likes = models.ManyToManyField(UserModel, related_name='liked_comment')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
