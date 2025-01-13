from django.contrib import admin
from .models import Event
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'organizer')
    list_filter = ('date', 'location', 'organizer')
    search_fields = ('title', 'description', 'location')
