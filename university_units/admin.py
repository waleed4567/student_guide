from django.contrib import admin
from .models import Office


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'location', 'manager', 'contact_number']
    search_fields = ['name', 'description__contains']
    list_filter = ['location']


