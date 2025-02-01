# CREM/urls.py

from django.contrib import admin
from django.urls import path
from . import views

# List of platforms
PLATFORMS = ['AIDE', 'ASMP', 'BIO', 'MSC', 'PCE', 'RESEE', 'SAI']

urlpatterns = [
    path('', views.home, name='home'), 
    path('contact/', views.contact, name='contact'),
]

# Generate URLs for each platform
for platform in PLATFORMS:
    urlpatterns += [
        path(f'{platform}/infrastructure/', getattr(views, f'{platform}_infrastructure'), name=f'{platform}_infrastructure'),
        path(f'{platform}/services/', getattr(views, f'{platform}_services'), name=f'{platform}_services'),
        path(f'{platform}/index/', getattr(views, f'{platform}_index'), name=f'{platform}_index'),
        path(f'{platform}/innovation/', getattr(views, f'{platform}_innovation'), name=f'{platform}_innovation'),
    ]