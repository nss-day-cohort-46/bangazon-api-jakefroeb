from django.urls import path
from .views import expensive_product_list, inexpensive_product_list, incomplete_order_list, favorited_sellers

urlpatterns = [
    path('reports/expensive_products', expensive_product_list),
    path('reports/inexpensive_products', inexpensive_product_list),
    path('reports/incomplete_orders', incomplete_order_list),
    path('reports/favorite_sellers', favorited_sellers)

]