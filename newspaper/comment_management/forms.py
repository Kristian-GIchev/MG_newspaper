from django import forms

from newspaper.comment_management.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class CreateCommentForm(CommentForm):
    pass


class EditCommentForm(CommentForm):
    pass


class DeleteCommentForm(CommentForm):
    pass
