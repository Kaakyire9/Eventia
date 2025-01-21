from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'profile_image', 'user_phone_number', 'address']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'profile_image', 'user_phone_number', 'address']