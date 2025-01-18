# filepath: /workspace/Eventia/user_profiles/management/commands/create_profiles.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user_profiles.models import UserProfile

class Command(BaseCommand):
    help = 'Create profiles for existing users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'profile'):
                UserProfile.objects.create(user=user)
        self.stdout.write(self.style.SUCCESS('Successfully created profiles for existing users'))