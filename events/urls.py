# urls.py
from django.urls import path
from .views import create_event, event_list, home, about, event_detail, update_event, delete_event, like_event, update_comment, delete_comment, request_attendance, approve_attendance, add_comment

urlpatterns = [
    path("", home, name="home"),  # Home page
    path("about/", about, name="about"),  # About page
    path("create/", create_event, name="create_event"),  # Create event
    path("events/", event_list, name="event_list"),  # List of events
    path("events/<int:pk>/", event_detail, name="event_detail"),  # Event details
    path("events/<int:pk>/update/", update_event, name="update_event"),  # Update event
    path("events/<int:pk>/delete/", delete_event, name="delete_event"),  # Delete event
    path("events/<int:pk>/like/", like_event, name="like_event"),  # Like event
    path("events/<int:event_id>/request_attendance/", request_attendance, name="request_attendance"),  # Request attendance
    path("attendees/<int:attendee_id>/approve/", approve_attendance, name="approve_attendance"),  # Approve attendance
    path("events/<int:event_id>/add_comment/", add_comment, name="add_comment"),  # Add comment
    path("comments/<int:pk>/update/", update_comment, name="update_comment"),  # Update comment
    path("comments/<int:pk>/delete/", delete_comment, name="delete_comment"),  # Delete comment
]
