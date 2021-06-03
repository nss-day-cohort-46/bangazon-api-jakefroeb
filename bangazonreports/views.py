from django.shortcuts import render
from bangazonapi.models import Product

# Create your views here.

def expensive_product_list(request):
    if request.method == "GET":
        products = Product.objects.filter(price__gte=1000)
        template = 'products/products.html'
        context = {'products' : products}
        return render(request, template, context)
def inexpensive_product_list(request):
    if request.method == "GET":
        products = Product.objects.filter(price__lt=1000)
        template = 'products/products.html'
        context = {'products' : products}
        return render(request, template, context)