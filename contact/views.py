from django.core.mail import send_mail, BadHeaderError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def contact(request):
    logger.info("Contact view function is being executed!")

    if request.method == "POST":
        logger.info("Received a POST request")

        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger.info(f"Received form data: Name={name}, Email={email}, Message={message}")

        # Validate email format
        try:
            validate_email(email)
        except ValidationError as e:
            logger.error(f"Email validation error: {e}")
            return redirect('/contact?status=invalid_email')

        # Email details
        subject = f"New Contact Form Submission from {name}"
        email_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        recipient_email = 'bouabbou@gmail.com'  # Replace with the target email address

        try:
            # Send email
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,  # Use your configured email
                [recipient_email],
                fail_silently=False,
            )
            logger.info("Email sent successfully!")
            return redirect('/contact?status=success')
        except BadHeaderError:
            logger.error("Invalid email header.")
            return redirect('/contact?status=error')
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            return redirect('/contact?status=error')

    logger.info("Rendering Contact_EN.html")
    return render(request, "Contact_EN.html")

