# CREM/urls.py

from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 
    # Admin site URL

    # Home page URL
    path('', views.home, name='home'),

    # Index page URL
    path('index/', views.index, name='index'),

    # Contact page URL
    path('contact/', views.contact, name='contact'),

    # Innovation page URL
    path('innovation/', views.innovation, name='innovation'),

    # Services page URL
    path('services/', views.services, name='services'),
    
    # Dynamic URL for platform's infrastructure
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('AAD_infrastructure/', views.AAD_infrastructure, name='AAD_infrastructure'),
    path('BABE_infrastructure/', views.BABE_infrastructure, name='BABE_infrastructure'),
    path('MSAC_infrastructure/', views.MSAC_infrastructure, name='MSAC_infrastructure'),
    path('PEACE_infrastructure/', views.PEACE_infrastructure, name='PEACE_infrastructure'),
    path('RESAN_infrastructure/', views.RESAN_infrastructure, name='RESAN_infrastructure'),
    path('SAI_infrastructure/', views.SAI_infrastructure, name='SAI_infrastructure'),
    
    #dynamic url from platform's presentation 
    path('services/', views.services, name='services'),
    path('AAD_services/', views.AAD_services, name='AAD_services'),
    path('BABE_services/', views.BABE_services, name='BABE_services'),
    path('MSAC_services/', views.MSAC_services, name='MSAC_services'),
    path('PEACE_services/', views.PEACE_services, name='PEACE_services'),
    path('RESAN_services/', views.RESAN_services, name='RESAN_services'),
    path('SAI_services/', views.SAI_services, name='SAI_services'),

    #dynamic url from platform's services
    path('index/', views.index, name='index'),
    path('AAD_index/', views.AAD_index, name='AAD_index'),
    path('BABE_index/', views.BABE_index, name='BABE_index'),
    path('MSAC_index/', views.MSAC_index, name='MSAC_index'),
    path('PEACE_index/', views.PEACE_index, name='PEACE_index'),
    path('RESAN_index/', views.RESAN_index, name='RESAN_index'),
    path('SAI_index/', views.SAI_index, name='SAI_index'),

]