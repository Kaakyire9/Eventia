# forms.py
from django import forms
from .models import Event, Comment

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location', 'image', 'video']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': 'required'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control',  'required': 'required'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control',  'required': 'required'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']