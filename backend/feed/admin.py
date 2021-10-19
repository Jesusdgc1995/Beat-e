from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created', 'user')
    list_filter = ('user','created')
    search_fields = ('user', 'content')
    ordering = ('created',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created', 'user', 'post')
    list_filter = ('user', 'post')
    search_fields = ('user', 'post', 'content')
    ordering = ('created',)