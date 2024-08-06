from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.email=email
        contact.message=message
        contact.save()
        
    return render(request, 'Contact_EN.html')
