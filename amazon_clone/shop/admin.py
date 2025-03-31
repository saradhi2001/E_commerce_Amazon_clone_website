from django.contrib import admin # type: ignore

# Register your models here.
from django.contrib import admin # type: ignore
from .models import Product, Cart

admin.site.register(Product)
admin.site.register(Cart)

