# views.py
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
import requests

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Validate reCAPTCHA
            recaptcha_response = form.cleaned_data.get('g_recaptcha_response')
            data = {
                'secret': 'YOUR_SECRET_KEY',
                'response': recaptcha_response
            }
            response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = response.json()
            
            if not result.get('success'):
                return render(request, 'contact.html', {'form': form, 'captcha_error': 'Invalid reCAPTCHA. Please try again.'})

            # Send email
            send_mail(
                subject=f"Message from {form.cleaned_data['name']} ({form.cleaned_data['email']})",
                message=form.cleaned_data['message'],
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['your_email@example.com'],
            )
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
