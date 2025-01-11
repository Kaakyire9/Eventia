# decorators.py
from django.http import HttpResponseForbidden

def organizer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'Organizer':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("You do not have permission to create events.")
    return wrapper