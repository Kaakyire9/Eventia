# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import EventForm
from .models import Event

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # Set the organizer to the current user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def event_list(request):
    events = Event.objects.filter(date__gte='2024-01-01').order_by('date')
    paginator = Paginator(events, 5)  # 5 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/event_list.html', {'page_obj': page_obj, 'post_list': page_obj})

def home(request):
    return render(request, 'events/event_list.html')

def about(request):
    return render(request, 'events/about.html')


