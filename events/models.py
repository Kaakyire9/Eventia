# models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} - {'Read' if self.is_read else 'Unread'}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/images/', null=True, blank=True)
    video = models.FileField(upload_to='events/videos/', null=True, blank=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_events")
    likes = models.ManyToManyField(User, related_name='liked_events', through='Like')
    is_canceled = models.BooleanField(default=False)  # Add this field back with a default value

    def __str__(self):
        return self.title

    def attendees_count(self):
        return self.attendees.filter(approved=True).count()

    def notify_attendees(self, message):
        """Notify all attendees about an update or cancellation."""
        attendees = self.attendees.filter(approved=True)
        for attendee in attendees:
            Notification.objects.create(user=attendee.user, message=message)

    def notify_organizer(self, message):
        """Notify the organizer about user cancellations or updates."""
        Notification.objects.create(user=self.organizer, message=message)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"Like by {self.user} on {self.event}"

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.event}"

class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    requested_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Attendee request by {self.user} for {self.event}"

    def cancel_attendance(self):
        """Cancel attendance and notify the organizer."""
        message = f"{self.user.username} has canceled attendance for '{self.event.title}'."
        self.event.notify_organizer(message)
        self.delete()


