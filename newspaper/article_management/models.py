from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()


class Article(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='article_img', blank=True)
    description = models.TextField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, default=None, null=True)

    class ArticleTypes(models.TextChoices):
        sports = 'sports'
        news = 'news'
        activities = 'activities'
        projects = 'projects'
        internships = 'internships'

    category = models.CharField(
        max_length=15,
        choices=ArticleTypes.choices,
        default=ArticleTypes.news,
        )
