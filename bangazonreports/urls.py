from django.urls import path
from .views import expensive_product_list

urlpatterns = [
    path('reports/expensive_products', expensive_product_list),
]