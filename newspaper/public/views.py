from django.shortcuts import render

from newspaper.comment_management.models import Comment
from newspaper.public.models import Article


def home(request):
    articles = Article.objects.order_by('-created_at')
    context = {
        'name': 'Home',
        'articles': articles
    }
    return render(request, 'public/index.html', context)


def about_us(request):

    context = {
        'name': 'About Us'
    }
    return render(request, 'public/index.html', context)


def news(request):
    articles = Article.objects.filter(category='news').order_by('-created_at')
    context = {
        'name': 'News',
        'articles': articles
    }
    return render(request, 'public/index.html', context)


def sports(request):
    articles = Article.objects.filter(category='sports').order_by('-created_at')
    context = {
        'name': 'Sports',
        'articles': articles
    }
    return render(request, 'public/index.html', context)


def activities(request):
    articles = Article.objects.filter(category='activities').order_by('-created_at')
    context = {
        'name': 'Activities',
        'articles': articles
    }
    return render(request, 'public/index.html', context)


def projects(request):
    articles = Article.objects.filter(category='projects').order_by('-created_at')

    context = {
        'name': 'Projects',
        'articles': articles
    }
    return render(request, 'public/index.html', context)


def internships(request):
    articles = Article.objects.filter(category='internships').order_by('-created_at')
    context = {
        'name': 'Internships',
        'articles': articles
    }
    return render(request, 'public/index.html', context)


def view_article(request, pk):
    article = Article.objects.get(pk=pk)
    is_liked = False
    if article.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'name': 'View Article',
        'article': article,
        'is_liked': is_liked,
    }
    return render(request, 'public/view_article.html', context)


# def view_comment(request, pk):
#     comment = Comment.objects.get(pk=pk)
#     is_liked = False
#     if comment.likes.filter(id=request.user.id).exists():
#         is_liked = True
#     context = {
#         'name': 'View Comment',
#         'comment': comment,
#         'is_liked': is_liked,
#     }
#     return render(request, 'public/view_comment.html', context)



# def web_dev(request):
#     context = {
#         'name': 'Web Development Club'
#     }
#     return render(request, 'index.html', context)
#
#
# def literature(request):
#     context = {
#         'name': 'Literature Club'
#     }
#     return render(request, 'index.html', context)
#
#
# def cinema(request):
#     context = {
#         'name': 'Cinema Club'
#     }
#     return render(request, 'index.html', context)

