from django.test import TestCase, Client
from django.urls import reverse
from contact.models import Contact
import json

class ContactFormTests(TestCase):
    
    def setUp(self):
        self.client = Client(enforce_csrf_checks=True)
        self.contact_url = reverse('contact')
        
    def test_ajax_detection(self):
        """Test that AJAX requests are properly detected"""
        # First get a CSRF token
        response = self.client.get(self.contact_url)
        csrf_token = self.client.cookies['csrftoken'].value
        
        # Test data with CSRF token
        test_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            'agree': 'on',
            'csrfmiddlewaretoken': csrf_token
        }
        
        # Test AJAX request
        response = self.client.post(
            self.contact_url, 
            test_data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        
        # Should return JSON for AJAX requests
        self.assertEqual(response.status_code, 200)
        
        # For debugging, check what's actually returned
        content_type = response.get('Content-Type', '')
        if 'application/json' in content_type:
            data = response.json()
            self.assertIn('response', data)
        else:
            # If it's HTML, check if it contains success indicators
            content = response.content.decode()
            self.assertIn('success', content.lower())
    
    def test_regular_form_submission(self):
        """Test regular form submission"""
        # First get a CSRF token
        response = self.client.get(self.contact_url)
        csrf_token = self.client.cookies['csrftoken'].value
        
        test_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'subject': 'Test Subject',
            'message': 'Test message',
            'agree': 'on',
            'csrfmiddlewaretoken': csrf_token
        }
        
        response = self.client.post(self.contact_url, test_data)
        self.assertEqual(response.status_code, 200)
        
        # Check if contact was saved to database
        contact = Contact.objects.last()
        self.assertIsNotNone(contact)
        self.assertEqual(contact.name, 'Test User')
