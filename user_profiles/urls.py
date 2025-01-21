from django.urls import path
from . import views
from .views import settings, reset_profile_image

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/reset_image/', views.reset_profile_image, name='reset_profile_image'),
    path('settings/', settings, name='settings'),
    path('reset_profile_image/', reset_profile_image, name='reset_profile_image'),
]
