from django import forms
from django.contrib.auth.models import User

from MG_vestnik.newspaper.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = 'title', 'description', 'image', 'category'


class CreateArticleForm(ArticleForm):
    pass


class EditArticleForm(ArticleForm):
    pass


class DeleteArticleForm(ArticleForm):
    pass
