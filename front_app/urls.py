# CREM/urls.py

from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), 

    # Contact page URL
    path('contact/', views.contact, name='contact'),
    
    # Dynamic URL for platform's infrastructure
    path('ASMP_infrastructure/', views.ASMP_infrastructure, name='ASMP_infrastructure'),
    path('AIDE_infrastructure/', views.AIDE_infrastructure, name='AIDE_infrastructure'),
    path('BIO_infrastructure/', views.BIO_infrastructure, name='BIO_infrastructure'),
    path('MSC_infrastructure/', views.MSC_infrastructure, name='MSC_infrastructure'),
    path('PCE_infrastructure/', views.PCE_infrastructure, name='PCE_infrastructure'),
    path('RESEE_infrastructure/', views.RESEE_infrastructure, name='RESEE_infrastructure'),
    path('SAI_infrastructure/', views.SAI_infrastructure, name='SAI_infrastructure'),
    
    #dynamic url from platform's presentation 
    path('ASMP_services/', views.ASMP_services, name='ASMP_services'),
    path('AIDE_services/', views.AIDE_services, name='AIDE_services'),
    path('BIO_services/', views.BIO_services, name='BIO_services'),
    path('MSC_services/', views.MSC_services, name='MSC_services'),
    path('PCE_services/', views.PCE_services, name='PCE_services'),
    path('RESEE_services/', views.RESEE_services, name='RESEE_services'),
    path('SAI_services/', views.SAI_services, name='SAI_services'),

    #dynamic url from platform's services
    path('ASMP_index/', views.ASMP_index, name='ASMP_index'),
    path('AIDE_index/', views.AIDE_index, name='AIDE_index'),
    path('BIO_index/', views.BIO_index, name='BIO_index'),
    path('MSC_index/', views.MSC_index, name='MSC_index'),
    path('PCE_index/', views.PCE_index, name='PCE_index'),
    path('RESEE_index/', views.RESEE_index, name='RESEE_index'),
    path('SAI_index/', views.SAI_index, name='SAI_index'),

     #dynamic url from platform's innovation
    path('ASMP_innovation/', views.ASMP_innovation, name='ASMP_innovation'),
    path('AIDE_innovation/', views.AIDE_innovation, name='AIDE_innovation'),
    path('BIO_innovation/', views.BIO_innovation, name='BIO_innovation'),
    path('MSC_innovation/', views.MSC_innovation, name='MSC_innovation'),
    path('PCE_innovation/', views.PCE_innovation, name='PCE_innovation'),
    path('RESEE_innovation/', views.RESEE_innovation, name='RESEE_innovation'),
    path('SAI_innovation/', views.SAI_innovation, name='SAI_innovation'),
    
    
  
]