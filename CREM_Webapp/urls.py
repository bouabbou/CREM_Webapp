# CREM_Webapp/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contact.views import Contact, contact

urlpatterns = [
    path('', contact, name='contact'),
    # Admin site URL
    path('admin/', admin.site.urls),

    # URLs for 'front_app'
    path('', include('front_app.urls')),  # Assuming 'front_app' has its own urls.py

    # URLs for 'instrumentation'
    path('instrumentation/', include('instrumentation.urls')),  # URLs for 'instrumentation' app

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
