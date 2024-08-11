# CREM/views.py
from django.templatetags.static import static

from django.shortcuts import render

from instrumentation.models import Category, Product

def home(request):
    return render(request, 'Home_EN.html')
def contact(request):
    return render(request, 'Contact_EN.html')
def infrastructure(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 


    }
    return render(request, 'Infrastructure_FA_EN.html', context)
def innovation(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 

 
    }
    return render(request, 'Innovation_FA_EN.html',context)
def services(request):
    context = {
        'logo': '../static/images/logo-grey.png',
        'link_color': 'grey', 

 
    }
    return render(request, 'Services_FA_EN.html',context)
def index(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 

 
    }
    return render(request, 'index_FA_EN.html',context)
def presentation(request):
    context = {
        'logo': '../static/images/logo-white.png',
        'link_color': 'white', 

 
    }
    return render(request, 'index_FA_EN.html',context)