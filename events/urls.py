# urls.py
from django.urls import path
from .views import create_event, event_list, home, about

urlpatterns = [
    path('about/', about, name='about'), 
    path('create/', create_event, name='create_event'),
    path('events/', event_list, name='event_list'),
    path('', home, name='home'),  # Add this line for the home page
]
