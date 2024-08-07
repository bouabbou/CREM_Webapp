# CREM/urls.py

from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    # Admin site URL

    # Home page URL
    path('', views.home, name='home'),

    # ADDITIVE/SUBTRACTIVE MANUFACTURING AND PROTOTYPING page URL
    path('AMP/', views.AMP, name='AMP'),

    # Contact page URL
    path('contact/', views.contact, name='contact'),

    # Infrastructure page URL
    path('infrastructure/', views.infrastructure, name='infrastructure'),

    # Innovation page URL
    path('innovation/', views.innovation, name='innovation'),

    # Services page URL
    path('services/', views.services, name='services'),

]
