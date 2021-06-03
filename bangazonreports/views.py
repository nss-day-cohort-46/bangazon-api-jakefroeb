from django.shortcuts import render
from bangazonapi.models import Product, Order
from django.db.models import Sum

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

def incomplete_order_list(request):
    if request.method == "GET":
        orders = Order.objects.filter(payment_type=None).annotate(total = Sum('lineitems__product__price'))
        template = 'orders/orders.html'
        context = {'orders' : orders}
        return render(request, template, context)