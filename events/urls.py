from django.urls import path
from .views import events_page_view

urlpatterns = [
    path("", events_page_view),
]