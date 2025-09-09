from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Test the contact form email functionality'

    def add_arguments(self, parser):
        parser.add_argument(
            '--email',
            type=str,
            help='Email address to send test to',
            default='a.bouabbou@ueuromed.org'
        )

    def handle(self, *args, **options):
        test_email = options['email']
        
        self.stdout.write(f"Testing email configuration to: {test_email}")
        self.stdout.write(f"Using EMAIL_HOST: {settings.EMAIL_HOST}")
        self.stdout.write(f"Using EMAIL_PORT: {settings.EMAIL_PORT}")
        self.stdout.write(f"Using EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
        self.stdout.write(f"Using DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
        
        subject = "Test Email from CREM Webapp Contact Form"
        message = """
        This is a test email to verify that the contact form email functionality is working correctly.
        
        If you received this email, the Microsoft 365 SMTP configuration is working properly.
        
        ---
        CREM Webapp Contact System
        """
        
        try:
            send_mail(
                subject,
                message.strip(),
                settings.DEFAULT_FROM_EMAIL,
                [test_email],
                fail_silently=False,
            )
            self.stdout.write(
                self.style.SUCCESS("✅ Email sent successfully!")
            )
            logger.info("Test email sent successfully to %s", test_email)
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Failed to send email: {e}")
            )
            logger.error("Failed to send test email: %s", e)
            
            # Provide troubleshooting tips
            self.stdout.write("\nTroubleshooting tips:")
            self.stdout.write("1. Check that EMAIL_HOST_PASSWORD environment variable is set")
            self.stdout.write("2. Verify Microsoft 365 credentials are correct")
            self.stdout.write("3. Ensure the account has SMTP sending permissions")
            self.stdout.write("4. Check firewall/network connectivity to smtp.office365.com")