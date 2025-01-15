# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import EventForm, CommentForm
from .models import Event, Like, Comment, Attendee

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
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

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    comments = event.comments.all()
    is_liked = event.likes.filter(user=request.user).exists()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            return redirect('event_detail', pk=event.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'events/event_detail.html', {
        'event': event,
        'comments': comments,
        'is_liked': is_liked,
        'comment_form': comment_form
    })

@login_required
def like_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    like, created = Like.objects.get_or_create(event=event, user=request.user)
    if not created:
        like.delete()
    if request.is_ajax():
        return JsonResponse({
            'like_count': event.likes.count(),
            'is_liked': created
        })
    return redirect('event_detail', pk=pk)

@login_required
def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/update_event.html', {'form': form})

@login_required
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_event.html', {'event': event})

@login_required
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this comment.")
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('event_detail', pk=comment.event.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'events/update_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this comment.")
    if request.method == 'POST':
        event_pk = comment.event.pk
        comment.delete()
        return redirect('event_detail', pk=event_pk)
    return render(request, 'events/delete_comment.html', {'comment': comment})

def home(request):
    # Get the current date
    current_date = timezone.now().date()

    # Get upcoming events (events that are closer)
    upcoming_events = Event.objects.filter(date__gte=current_date).order_by('date')[:6]

    # Calculate the number of days left for each event
    for event in upcoming_events:
        event.days_left = (event.date - current_date).days

    return render(request, 'home.html', {'upcoming_events': upcoming_events})

def about(request):
    return render(request, 'events/about.html')

@login_required
def request_attendance(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendee, created = Attendee.objects.get_or_create(event=event, user=request.user)
    if created:
        # New request created
        attendee.requested_at = timezone.now()
        attendee.save()
    return redirect('event_detail', event_id=event.id)

@login_required
def approve_attendance(request, attendee_id):
    attendee = get_object_or_404(Attendee, id=attendee_id)
    if request.user == attendee.event.organizer:  # Assuming Event has an organizer field
        attendee.approved = True
        attendee.approved_at = timezone.now()
        attendee.save()
    return redirect('event_detail', event_id=attendee.event.id)


