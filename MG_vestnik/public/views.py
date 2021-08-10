from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from MG_vestnik.public.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm
from MG_vestnik.public.models import Article
from MG_vestnik.settings import LOGIN_URL


def home(request):
    new = Article.objects.filter(category='news').order_by('-created_at')[0]
    sport = Article.objects.filter(category='sports').order_by('-created_at')[0]
    activities = Article.objects.filter(category='activities').order_by('-created_at')[0]
    school_projects = Article.objects.filter(category='school_projects').order_by('-created_at')[0]
    international_internships = Article.objects.filter(category='international_internships').order_by('-created_at')[0]
    articles = [new, sport, activities, school_projects, international_internships]
    context = {
        'name': 'Home',
        'articles': articles
    }
    return render(request, 'index.html', context)


def about_us(request):
    context = {
        'name': 'About Us'
    }
    return render(request, 'index.html', context)


def news(request):
    articles = Article.objects.filter(category='news').order_by('-created_at')
    context = {
        'name': 'News',
        'articles': articles
    }
    return render(request, 'index.html', context)


def sports(request):
    articles = Article.objects.filter(category='sports').order_by('-created_at')
    context = {
        'name': 'Sports',
        'articles': articles
    }
    return render(request, 'index.html', context)


def activities(request):
    articles = Article.objects.filter(category='activities').order_by('-created_at')
    context = {
        'name': 'Activities',
        'articles': articles
    }
    return render(request, 'index.html', context)


def school_projects(request):
    articles = Article.objects.filter(category='school_projects').order_by('-created_at')
    context = {
        'name': 'School Projects',
        'articles': articles
    }
    return render(request, 'index.html', context)


def international_internships(request):
    articles = Article.objects.filter(category='international_internships').order_by('-created_at')
    context = {
        'name': 'International Internships',
        'articles': articles
    }
    return render(request, 'index.html', context)


def web_dev(request):
    context = {
        'name': 'Web Development Club'
    }
    return render(request, 'index.html', context)


def literature(request):
    context = {
        'name': 'Literature Club'
    }
    return render(request, 'index.html', context)


def cinema(request):
    context = {
        'name': 'Cinema Club'
    }
    return render(request, 'index.html', context)


@login_required(login_url=LOGIN_URL)
def view_my_articles(request):
    user = request.user
    articles = user.article_set
    context = {
        'articles': articles,
        'name': 'View My Articles',
    }
    return render(request, 'view_my_articles.html', context)


@login_required(login_url=LOGIN_URL)
def create_article(request):
    form = CreateArticleForm(request.POST, request.FILES)
    if form.is_valid():

        form.save()
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

