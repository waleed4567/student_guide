from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'author']
    search_fields = ['title', 'body__contains']
    list_filter = ['author']

