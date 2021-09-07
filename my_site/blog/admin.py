from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "author", "date"]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["text", "first_name", "last_name", "post"]
    list_filter = ["first_name", "last_name"]

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
