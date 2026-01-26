from django.contrib import admin
from .models import Department, Product

# Basic registration
admin.site.register(Department)
admin.site.register(Product)