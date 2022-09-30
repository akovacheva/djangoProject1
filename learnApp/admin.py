from django.contrib import admin
from .models import Post, Comment, QuesModel


# Register your models here.

class CommentAdmin (admin.ModelAdmin):
    model = Comment
    extra = 0
    list_display = ("user","last_modified",'title')

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user")
    search_fields = ("title", "content")

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return  True
        return False # da ne moze promena na postovite

    def get_readonly_fields(self, request, obj=None):
        if obj is not None and obj.user == request.user:
            return []
        if obj is None:
            return []
        return [
            "title",
            "content",
            "user",
            "date_created",
            "last_modified",
        ]

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user == request.user:
            return True
        return False

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(QuesModel)
