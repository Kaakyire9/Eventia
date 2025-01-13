from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'organizer')
    list_filter = ('date', 'location', 'organizer')
    search_fields = ('title', 'description', 'location')
