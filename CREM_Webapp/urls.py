# CREM_Webapp/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contact.views import contact

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # URLs for 'front_app'
    path('', include('front_app.urls')),  # Assuming 'front_app' has its own urls.py

    # URLs for 'instrumentation'
    path('instrumentation/', include('instrumentation.urls')),  # URLs for 'instrumentation' app
    path('contact/', include('contact.urls')),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Robots.txt - serve static file directly
from django.views.static import serve
from django.conf import settings

urlpatterns += [
    path('robots.txt', serve, {'document_root': settings.STATICFILES_DIRS[0], 'path': 'robots.txt'}),
]
