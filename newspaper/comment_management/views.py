from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from newspaper.article_management.models import Article
from newspaper.comment_management.forms import CreateCommentForm, EditCommentForm, DeleteCommentForm
from newspaper.comment_management.models import Comment
from newspaper.core.functions import make_readonly
from newspaper.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def view_my_comments(request):
    user = request.user
    comments = Comment.objects.filter(user=user)
    context = {
        'comments': comments,
        'name': 'View My Comments',
    }
    return render(request, 'comment_management/view_my_comments.html', context)


@login_required(login_url=LOGIN_URL)
def create_comment(request, article_pk):
    commented_article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        form = CreateCommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = Comment.objects.create(article=commented_article,
                                             user=request.user,
                                             content=form.cleaned_data.get('content')
                                             )
            comment.save()
            return redirect('view_article', comment.article.id)
    else:
        form = CreateCommentForm()
    context = {
        'form': form,
        'article_pk': article_pk,
        'name': 'Create New Comment',
    }
    return render(request, 'comment_management/create_comment.html', context)


@login_required(login_url=LOGIN_URL)
def edit_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditCommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('view_article', comment.article.id)
    else:
        form = EditCommentForm(instance=comment)
    context = {
        'form': form,
        'comment': comment,
        'name': 'Edit Comment',
    }
    return render(request, 'comment_management/edit_comment.html', context)


@login_required(login_url=LOGIN_URL)
def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteCommentForm(request.POST, request.FILES, instance=comment)
        art_id = comment.article.id
        comment.delete()
        return redirect('view_article', art_id)
    else:
        form = DeleteCommentForm(instance=comment)
    context = {
        'form': form,
        'name': 'Delete Comment',
        'comment': comment,
    }
    return render(request, 'comment_management/delete_comment.html', context)


@login_required(login_url=LOGIN_URL)
def like_comment(request, pk):

    comment = get_object_or_404(Comment, id=request.POST.get('article_id'))
    if comment.likes.filter(id=request.user.id).exists():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)

    return HttpResponseRedirect(reverse('view_article', args=[comment.article.pk]))
