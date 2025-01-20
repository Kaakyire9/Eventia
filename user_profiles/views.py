from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
import logging

logger = logging.getLogger(__name__)

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    logger.info("Profile: %s", profile)
    logger.info("Bio: %s", profile.bio)
    logger.info("Location: %s", profile.location)
    logger.info("Birth Date: %s", profile.birth_date)
    return render(request, 'user_profiles/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profiles/edit_profile.html', {'form': form})

@login_required
def reset_profile_image(request):
    profile = request.user.profile
    profile.profile_image = 'placeholder'  # Set to the public ID of the placeholder image
    profile.save()
    return redirect('profile')

