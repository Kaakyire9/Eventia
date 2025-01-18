from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            logger.info("Profile saved successfully")
            logger.info("Saved Bio: %s", profile.bio)
            logger.info("Saved Location: %s", profile.location)
            logger.info("Saved Birth Date: %s", profile.birth_date)
            return redirect('profile')
        else:
            logger.error("Form is not valid: %s", form.errors)
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profiles/edit_profile.html', {'form': form})

