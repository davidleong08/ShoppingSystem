from django.contrib import admin
from apps.order.models import *


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"
    # the attributes of showing in list
    list_display = ['purchase_order_number', 'total_order_amount', 'purchase_order_status',
                    'shipped_date', 'cancelDate', 'user']
    # search
    search_fields = ['purchase_order_number', 'user', 'product']
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
    list_display = ['shopping_cart_id', 'product', 'count_number']
    # search
    search_fields = ['shopping_cart_id', 'product']
    # filtration
    list_filter = ['shopping_cart_id']
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['shopping_cart_id']


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"
    # the attributes of showing in list
    list_display = ['order_list_number', 'total_price', 'total_number', 'product', 'order']
    # search
    search_fields = ['order_list_number']
    # filtration
    list_filter = ['order_list_number', 'total_price', 'total_number']
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['order_list_number']

