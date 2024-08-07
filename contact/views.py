from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
        
    return render(request, 'Contact_EN.html') 
