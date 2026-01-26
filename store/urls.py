# store/urls.py - URL routing
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.all_products, name='all_products'),      # All products list
    path('search/', views.search_product, name='search_product'),    # Search functionality
]