from django.contrib import admin

from newspaper.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'article', 'user', 'created',)
    list_filter = ('article', 'user', 'created', 'updated')
    search_fields = ('content',)

