from django.shortcuts import render

from instrumentation.models import Product

# Create your views here.
def products(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'products.html', {'products': products})