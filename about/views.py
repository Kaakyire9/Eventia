from django.shortcuts import render, redirect
from django.contrib import messages

def about(request):
    return render(request, 'about/about.html')

def contact(request):
    return render(request, 'about/contact.html')


def contact_view(request):
    if request.method == 'POST':
        # Process form submission
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')


