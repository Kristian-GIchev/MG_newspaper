from django.contrib.auth import get_user_model
from django.db import models

from newspaper.article_management.models import Article


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)


class QOTD(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
