from django.contrib import admin
from .models import Chapter, GuideTopic

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['number', 'title']

@admin.register(GuideTopic)
class GuideTopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'created', 'updated']
    search_fields = ['title', 'content__contains']
    list_filter = ['title']
