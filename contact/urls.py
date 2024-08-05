from django.urls import path, include
from contact.views import contact, success

urlpatterns = [
    path('', contact, name='contact'),
    path('success/', success, name='success'),
]