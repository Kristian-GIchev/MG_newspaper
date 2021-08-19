from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

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
    return render(request, 'article_management/view_my_articles.html', context)


@login_required(login_url=LOGIN_URL)
def create_article(request):
    if request.method == "POST":
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article.objects.create(title=form.cleaned_data.get('title'),
                                             description=form.cleaned_data.get('description'),
                                             image=form.cleaned_data.get('image'),
                                             category=form.cleaned_data.get('category'),
                                             user=request.user,
                                             )
            article.save()
            return redirect('view_my_articles')
    else:
        form = CreateArticleForm()
    context = {
        'form': form,
        'name': 'Create New Article',
    }
    return render(request, 'article_management/create_article.html', context)


@login_required(login_url=LOGIN_URL)
def edit_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('view_my_articles')
    else:
        form = EditArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
        'name': 'Edit Article',
    }
    return render(request, 'article_management/edit_article.html', context)


@login_required(login_url=LOGIN_URL)
def delete_article(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteArticleForm(request.POST, request.FILES, instance=article)
        article.delete()
        return redirect('view_my_articles')
    else:
        form = DeleteArticleForm(instance=article)
    context = {
        'form': form,
        'name': 'Delete Article',
        'article': article,
    }
    return render(request, 'article_management/delete_article.html', context)


@login_required(login_url=LOGIN_URL)
def like_article(request, pk):

    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:
        article.likes.add(request.user)

    return HttpResponseRedirect(reverse('view_article', args=[str(pk)]))

