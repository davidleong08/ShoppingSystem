from django.contrib import admin
from apps.basic.models import *


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"
    # the attributes of showing in list
    list_display = ['shipping_id', 'user', 'receiver_name', 'receiver_phone', 'receiver_mobile', 'receiver_province',
                    'receiver_city', 'receiver_district', 'receiver_address', 'receiver_zip', 'create_time']
    # search
    search_fields = ['shipping_id', 'user']
    # filtration
    list_filter = ['shipping_id', 'user']
    # Set the date selector
    date_hierarchy = 'create_time'
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['shipping_id']

