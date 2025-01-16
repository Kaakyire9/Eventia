# urls.py
from django.urls import path
from .views import create_event, event_list, home, about, event_detail, update_event, delete_event, like_event, update_comment, delete_comment, request_attendance, approve_attendance, add_comment

urlpatterns = [
    path('about/', about, name='about'), 
    path('create/', create_event, name='create_event'),
    path('events/', event_list, name='event_list'),
    path('events/<int:pk>/', event_detail, name='event_detail'),
    path('events/<int:pk>/update/', update_event, name='update_event'),
    path('events/<int:pk>/delete/', delete_event, name='delete_event'),
    path('events/<int:pk>/like/', like_event, name='like_event'),
    path('comments/<int:pk>/update/', update_comment, name='update_comment'),
    path('comments/<int:pk>/delete/', delete_comment, name='delete_comment'),
    path('events/<int:event_id>/request_attendance/', request_attendance, name='request_attendance'),
    path('attendees/<int:attendee_id>/approve/', approve_attendance, name='approve_attendance'),
    path('events/<int:event_id>/add_comment/', add_comment, name='add_comment'),
    path('', home, name='home'),  # Home page
]
