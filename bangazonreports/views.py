from django.shortcuts import render
from bangazonapi.models import Product

# Create your views here.

def expensive_product_list(request):
    if request.method == "GET":
        products = Product.objects.filter(price__gte=1000)
        template = 'products/expensive_products.html'
        context = {'products' : products}
        return render(request, template, context)
