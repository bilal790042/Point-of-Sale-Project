from django.contrib import admin
from .models import Product, Order

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Order)

admin.site.site_header = 'Sale of Point Project'

# now i am applying the read products which are saved for us not pre-loaded