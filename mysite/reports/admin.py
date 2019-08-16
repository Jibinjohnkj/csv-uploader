from django.contrib import admin

# Register your models here.

from reports.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('catalog_no', 'quantity', 'catalog_price')

admin.site.register(Product, ProductAdmin)

