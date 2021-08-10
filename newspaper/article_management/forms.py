from django import forms
from newspaper.article_management.models import Article


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
