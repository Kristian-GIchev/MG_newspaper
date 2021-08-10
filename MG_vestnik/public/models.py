from django.contrib.auth import get_user_model
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='article_img', blank=True)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, default=None, null=True)

    class ArticleTypes(models.TextChoices):
        sports = 'sports'
        news = 'news'
        activities = 'activities'
        school_projects = 'school_projects'
        international_internships = 'international_internships'

    category = models.CharField(
        max_length=25,
        choices=ArticleTypes.choices,
        default=ArticleTypes.news,
        )


class Like(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)


class QOTD(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=150)
