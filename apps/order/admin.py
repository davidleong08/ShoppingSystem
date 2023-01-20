from django.contrib import admin
from apps.order.models import *


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"
    # the attributes of showing in list
    list_display = ['purchase_order_number', 'purchase_date', 'total_order_amount', 'purchase_order_status', 'customer',
                    'shipped_date', 'product']
    # search
    search_fields = ['purchase_order_number', 'customer', 'product']
    # filtration
    list_filter = ['purchase_order_number']
    # Set the date selector
    date_hierarchy = 'shipped_date'
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['purchase_order_number']


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"
    # the attributes of showing in list
    list_display = ['shopping_cart_id', 'purchase_order', 'product', 'category', 'count_number', 'total_price']
    # search
    search_fields = ['shopping_cart_id', 'purchase_order', 'product', 'category']
    # filtration
    list_filter = ['shopping_cart_id', 'purchase_order', 'category']
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['shopping_cart_id']


