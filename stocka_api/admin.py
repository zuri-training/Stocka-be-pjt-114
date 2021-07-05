from django.contrib import admin
from .models import (Product, Sale, Purchase, Vendor, Category)

# Register your models here.
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Purchase)
admin.site.register(Category)
admin.site.register(Vendor)
