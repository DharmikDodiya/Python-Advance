from django.contrib import admin
from catalog.models import Product

# Register your models here.
# First Why
# admin.site.register(Product)

# Second Why
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'price', 'stock', 'created_at', 'updated_at')
    
# admin.site.register(Product, ProductAdmin)

# Third Why
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock')