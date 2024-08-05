# CREM/views.py
from django.templatetags.static import static

from django.shortcuts import render

def home(request):
    return render(request, 'Home_EN.html')
def contact(request):
    return render(request, 'Contact_EN.html')
def infrastructure(request):
    return render(request, 'Infrastructure_FA_EN.html')
def innovation(request):
    return render(request, 'Innovation_FA_EN.html')
def services(request):
    return render(request, 'Services_FA_EN.html')
def index(request):
    return render(request, 'index_FA_EN.html')
def presentation(request):
    return render(request, 'index_FA_EN.html')