from django.contrib import admin

from .models import Product, Service, CartItem, Order

admin.site.register(Product)
admin.site.register(Service)
admin.site.register(CartItem)

admin.site.register(Order)
