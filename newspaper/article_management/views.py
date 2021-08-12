from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from newspaper.article_management.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm
from newspaper.public.models import Article
from newspaper.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def view_my_articles(request):
    user = request.user
    articles = Article.objects.filter(user=user)
    context = {
        'articles': articles,
        'name': 'View My Articles',
    }
    return render(request, 'view_my_articles.html', context)


@login_required(login_url=LOGIN_URL)
def create_article(request):
    form = CreateArticleForm(request.POST, request.FILES)
    if form.is_valid():
        article = Article.objects.create(title=form.cleaned_data.get('title'),
                                         description=form.cleaned_data.get('description'),
                                         image=form.cleaned_data.get('image'),
                                         category=form.cleaned_data.get('category'),
                                         user=request.user,
                                         )
        article.save()
        return redirect('home')
    context = {
        'form': form,
        'name': 'Create New Article',
    }
    return render(request, 'create_article.html', context)


@login_required(login_url=LOGIN_URL)
def edit_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
        'name': 'Edit Article',
    }
    return render(request, 'edit_article.html', context)


@login_required(login_url=LOGIN_URL)
def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteArticleForm(request.POST, request.FILES, instance=article)
        article.delete()
        return redirect('home')
    else:
        form = DeleteArticleForm(instance=article)
    context = {
        'form': form,
        'name': 'Edit Article',
        'article': article,
    }
    return render(request, 'delete_article.html', context)


def view_article(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'name': 'View Article',
        'article': article,
    }
    return render(request, 'single_article.html', context)
