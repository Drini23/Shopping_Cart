from django.contrib import admin
from .models import Cart, CartItem, Collection, Product, Promotion

# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Promotion)

