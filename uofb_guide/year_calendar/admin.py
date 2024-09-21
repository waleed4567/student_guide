from django.contrib import admin
from .models import EventType, Event


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['college', 'title', 'description', 'date', 'added_at']
    search_fields = ['title', 'college', 'description__contains']
    list_filter = ['college']
    