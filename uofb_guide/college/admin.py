from django.contrib import admin
from .models import Anouncement, College, Batch

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location']


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    pass


@admin.register(Anouncement)
class AnouncementAdmin(admin.ModelAdmin):
    list_display = ['college', 'title', 'body', ]
    search_fields = ['title', 'body__contains']
    list_filter = ['college']


