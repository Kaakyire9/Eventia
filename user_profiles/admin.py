# filepath: /workspace/Eventia/user_profiles/admin.py
from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'location', 'birth_date', 'user_phone_number', 'address')
    search_fields = ('user__username', 'bio', 'location', 'user_phone_number', 'address')
