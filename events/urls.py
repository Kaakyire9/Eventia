# urls.py
from django.urls import path
from .views import create_event, event_list, home, about, event_detail, update_event, delete_event

urlpatterns = [
    path('about/', about, name='about'), 
    path('create/', create_event, name='create_event'),
    path('events/', event_list, name='event_list'),
    path('events/<int:pk>/', event_detail, name='event_detail'),
    path('events/<int:pk>/update/', update_event, name='update_event'),  # Add this line for the update event view
    path('events/<int:pk>/delete/', delete_event, name='delete_event'),  # Add this line for the delete event view
    path('', home, name='home'),  # Home page
]
