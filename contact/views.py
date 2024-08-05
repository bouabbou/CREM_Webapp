from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        message=request.POST['message']

        send_mail('Contact form',
                  message,
                  settings.EMAIL_HOST_USER,
                  ['elhammamimeryem@gmail.com'], 
                  fail_silently=False)
        
    return render(request, 'Contact_FA_EN.html')
    
def success(request):
    return render(request, 'success.html')