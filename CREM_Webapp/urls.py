# CREM_Webapp/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.home, name='home'),  
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('infrastructure/', views.infrastructure, name='infrastructure'),
    path('innovation/', views.innovation, name='innovation'),
    path('services/', views.services, name='services'),
    path('',include('contact.urls')),
    
]
=======

    # URLs for 'front_app'
    path('', include('front_app.urls')),  # Assuming 'front_app' has its own urls.py

    # URLs for 'instrumentation'
    path('instrumentation/', include('instrumentation.urls')),  # URLs for 'instrumentation' app

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a4c9d630d0a7ade70c46d0961c35bb76e279776a
