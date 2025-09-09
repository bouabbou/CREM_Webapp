from django.core.mail import send_mail, BadHeaderError
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import Contact
import logging

logger = logging.getLogger(__name__)

def contact(request):
    logger.info("Contact view function is being executed!")

    if request.method == "POST":
        logger.info("Received a POST request")
        logger.info(f"POST data: {dict(request.POST)}")
        logger.info(f"Request headers: {dict(request.headers)}")
        
        # Debug AJAX detection - check both META and headers
        x_requested_with_meta = request.META.get('HTTP_X_REQUESTED_WITH')
        x_requested_with_headers = request.headers.get('X-Requested-With')
        logger.info(f"META HTTP_X_REQUESTED_WITH: {x_requested_with_meta}")
        logger.info(f"Headers X-Requested-With: {x_requested_with_headers}")
        
        # Check all relevant headers for AJAX detection
        ajax_headers = {k: v for k, v in request.META.items() if 'HTTP' in k or 'X_' in k}
        logger.info(f"Relevant headers: {ajax_headers}")
        
        # Test different AJAX detection methods
        is_ajax = (
            request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' or
            request.headers.get('X-Requested-With') == 'XMLHttpRequest' or
            request.META.get('HTTP_X_REQUESTED_WITH') == 'xmlhttprequest' or
            request.headers.get('X-Requested-With') == 'xmlhttprequest'
        )
        logger.info(f"Is AJAX request: {is_ajax}")

        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        agree = request.POST.get('agree')  # Check if terms are agreed

        logger.info(f"Received form data: Name={name}, Email={email}, Message={message}, Agree={agree}")
        
        # Debug: Check if form data is missing
        if not all([name, email, message, agree]):
            logger.error("Missing form data - check form field names")
            logger.error(f"Available POST keys: {list(request.POST.keys())}")
            logger.error(f"Missing fields: name={name is None}, email={email is None}, message={message is None}, agree={agree is None}")
            
            # Handle AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'response': 'error', 'message': 'Missing form data'})
            return redirect('/contact?status=error')

        # Check if terms are agreed
        if not agree:
            logger.error("User did not agree to terms of service")
            
            # Handle AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'response': 'error', 'message': 'Please agree to terms of service'})
            return redirect('/contact?status=error')

        # Validate email format
        try:
            validate_email(email)
        except ValidationError as e:
            logger.error(f"Email validation error: {e}")
            
            # Handle AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'response': 'error', 'message': 'Invalid email address'})
            return redirect('/contact?status=invalid_email')

        # Save to database first
        try:
            contact = Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            logger.info(f"Contact saved to database with ID: {contact.id}")
        except Exception as e:
            logger.error(f"Failed to save contact to database: {e}")
            # Continue with email even if database save fails

        # Email details
        subject = f"New Contact Form Submission from {name}"
        email_message = f"""
        New contact form submission received:

        Name: {name}
        Email: {email}
        
        Message:
        {message}
        
        ---
        This message was sent from CREM Webapp contact form.
        """
        recipient_email = 'labs@ueuromed.org'  # Your admin email

        try:
            # Send email notification
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient_email],
                fail_silently=False,
            )
            logger.info(f"Email sent successfully to {recipient_email}")
            
            # Handle AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'response': 'success', 'message': 'Message sent successfully!'})
            return redirect('/contact?status=success')
        except BadHeaderError:
            logger.error("Invalid email header.")
            
            # Handle AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'response': 'error', 'message': 'Invalid email header'})
            return redirect('/contact?status=error')
        except Exception as e:
            logger.error(f"Error sending email: {e}")
            logger.error(f"Email error details: {type(e).__name__}: {str(e)}")
            import traceback
            logger.error(f"Full traceback: {traceback.format_exc()}")
            
            # Check if it's an authentication error
            if "authentication" in str(e).lower() or "credentials" in str(e).lower():
                logger.error("EMAIL AUTHENTICATION ERROR: Check Gmail credentials and app password")
                # Still return success since message is in database
                
                # Handle AJAX request
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'response': 'success', 'message': 'Message received! (Email delivery failed)'})
                return redirect('/contact?status=success')
            else:
                # For other errors, still return success but log the issue
                logger.error("Email failed but returning success - message saved to database")
                
                # Handle AJAX request
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'response': 'success', 'message': 'Message received! (Email delivery failed)'})
                return redirect('/contact?status=success')

    logger.info("Rendering Contact_EN.html")
    return render(request, "Contact_EN.html")

