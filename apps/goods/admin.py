from django.contrib import admin
from apps.goods.models import *


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"

    # the attributes of showing in list
    list_display = ['product_id', 'name', 'market_price', 'category', 'price', 'unit', 'amount', 'click_num', 'fav_num',
                    'goods_desc', 'main_image', 'stock_num', 'createDate']
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
    list_display = ['category_id', 'name', 'level', 'sort', 'createDate']
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


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    admin.site.site_title = "ShoppingSystem Admin"
    admin.site.site_header = "ShoppingSystem Admin"
    admin.site.index_title = "ShoppingSystem Management"
    # the attributes of showing in list
    list_display = ['slide_id', 'product', 'images', 'sort', 'create_date']
    # search
    search_fields = ['slide_id']
    # filtration
    list_filter = ['slide_id']
    # set the date selector
    date_hierarchy = 'create_date'
    # Set the amount of data displayed per page
    list_per_page = 10
    # Set the sort
    ordering = ['slide_id']
