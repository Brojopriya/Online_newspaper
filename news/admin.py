from django.contrib import admin
from .models import Article, Comment

class CommentAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        return False  # Cannot edit comments

admin.site.register(Article)
admin.site.register(Comment, CommentAdmin)
