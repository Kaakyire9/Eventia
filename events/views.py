# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, JsonResponse
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import EventForm, CommentForm
from .models import Event, Like, Comment, Attendee
from django.contrib import messages
from django.db.models import Count

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user  # Set the organizer to the current user
            event.save()
            messages.success(request, f'Event "{event.title}" successfully created!')
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def event_list(request):
    sort_by = request.GET.get('sort_by', 'date_desc')
    if sort_by == 'date_asc':
        events = Event.objects.all().order_by('date')
    elif sort_by == 'date_desc':
        events = Event.objects.all().order_by('-date')
    elif sort_by == 'title_asc':
        events = Event.objects.all().order_by('title')
    elif sort_by == 'title_desc':
        events = Event.objects.all().order_by('-title')
    elif sort_by == 'popularity':
        events = Event.objects.all().annotate(like_count=Count('likes')).order_by('-like_count')
    else:
        events = Event.objects.all().order_by('-date')

    paginator = Paginator(events, 6)  # Show 6 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'events/event_list.html', {'page_obj': page_obj, 'sort_by': sort_by})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    attendance_requested = None
    if request.user.is_authenticated:
        attendance_requested = event.attendees.filter(user=request.user).first()
    comments = Comment.objects.filter(event=event).order_by('-created_at')  # Order by created_at descending
    comment_form = CommentForm()
    context = {
        'event': event,
        'attendance_requested': attendance_requested,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'events/event_detail.html', context)

@login_required
def like_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, event=event)
    if not created:
        like.delete()
        is_liked = False
    else:
        is_liked = True
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'is_liked': is_liked,
            'like_count': event.likes.count()
        })
    return redirect('event_detail', pk=event.pk)

@login_required
def update_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
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

@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.user = request.user
            comment.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'comment': {
                        'pk': comment.pk,
                        'content': comment.content,
                        'user': comment.user.username,
                        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    },
                    'comment_count': event.comments.count()
                })
            return redirect('event_detail', pk=event.id)
    return JsonResponse({'success': False})

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
        messages.success(request, 'Request has been submitted and is waiting for approval.')
    else:
        messages.info(request, 'You have already requested to attend this event.')
    return redirect('event_detail', pk=event.id)

@login_required
def approve_attendance(request, attendee_id):
    attendee = get_object_or_404(Attendee, id=attendee_id)
    if request.user == attendee.event.organizer:  # Assuming Event has an organizer field
        attendee.approved = True
        attendee.approved_at = timezone.now()
        attendee.save()
        messages.success(request, 'Attendance request has been approved.')
    return redirect('event_detail', pk=attendee.event.id)

def events_by_type(request, event_type):
    events = Event.objects.filter(type=event_type)
    return render(request, f'events/{event_type}_type.html', {'events': events})


