from django.contrib.auth import get_user_model
from django.db import models

from newspaper.article_management.models import Article
# from newspaper.public.models import Like

UserModel = get_user_model()


# class Comment(models.Model):
#     content = models.TextField(
#         max_length=500,
#     )
#     user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     like = models.ForeignKey(Like, on_delete=models.DO_NOTHING)
