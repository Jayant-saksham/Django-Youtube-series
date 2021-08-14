from django.contrib import admin
from store.models.category import Category
from store.models.product import Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
