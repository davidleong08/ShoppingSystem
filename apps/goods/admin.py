from django.contrib import admin
from apps.goods.models import *


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"

    # the attributes of showing in list
    list_display = ['product_id', 'name', 'category', 'price', 'main_image', 'createDate', 'property1', 'property2',
                    'sale_number', 'sale_amount', 'customer_rating', 'review', 'temporary_status']
    # search
    search_fields = ['product_id', 'name', 'category', 'createDate']
    # filtration
    list_filter = ['product_id', 'category']
    # Set the date selector
    date_hierarchy = 'createDate'
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['product_id']


@admin.register(ProductsCategory)
class ProductsCategoryAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"

    # the attributes of showing in list
    list_display = ['category_id', 'name', 'createDate']
    # search
    search_fields = ['category_id', 'name']
    # filtration
    list_filter = ['category_id', 'name', 'createDate']
    # Set the date selector
    date_hierarchy = 'createDate'
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['category_id']


