from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        # Send an email
        try:
            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=message,
                from_email=email,
                recipient_list=['elhammamimeryem@gmail.com'],
                fail_silently=False,
            )
            return redirect('/contact/?status=success')
        except Exception as e:
            return redirect('/contact/?status=error')

    return render(request, 'Contact_EN.html')

