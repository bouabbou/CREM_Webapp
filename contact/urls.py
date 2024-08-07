from django.urls import path, include
from . import views
from contact.views import contact

urlpatterns = [
    path('/contact', views.Contact, name='contact'),
]