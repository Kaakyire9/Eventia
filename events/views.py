from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def events_page_view(request):
    return HttpResponse("This is an events page")
