from django import forms
from .models import Contact

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'fname', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'placeholder': 'Email address'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Message', 'rows': 5}),
        }