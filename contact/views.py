from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method=='POST':
        contact=Contact()
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return HttpResponse("Message sent successfully")
        
    return render(request, 'Contact_FA_EN.html')