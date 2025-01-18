from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = CloudinaryField('image', default='placeholder')  # Use the public ID of the uploaded image
    user_phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username

    def reset_profile_image(self):
        self.profile_image = 'placeholder'  # Set to the public ID of the placeholder image
        self.save()
