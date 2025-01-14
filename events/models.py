# models.py
from django.db import models
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200, blank=True, null=True)  # Allow null values
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    video = models.FileField(upload_to='event_videos/', blank=True, null=True)

    def __str__(self):
        return self.title

