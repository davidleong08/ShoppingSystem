from datetime import datetime

from django.db import models


# Create your models here.


class ProductsCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    level = models.IntegerField()
    sort = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.category_id) + self.name

    class Meta:
        verbose_name = 'products category'
        verbose_name_plural = 'product categories'
        db_table = 'd_productsCategory'


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    market_price = models.DecimalField(max_digits=32, decimal_places=8)
    category = models.ForeignKey(ProductsCategory, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=32, decimal_places=8)
    unit = models.CharField(max_length=10)
    amount = models.IntegerField()
    click_num = models.IntegerField()
    fav_num = models.IntegerField()
    goods_desc = models.TextField(max_length=5000)
    main_image = models.CharField(max_length=5000)
    stock_num = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product_id) + self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        db_table = 'd_product'


# slide picture
class Slide(models.Model):
    slide_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    images = models.ImageField(upload_to='slide', verbose_name='slide picture')
    sort = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.slide_id)

    class Meta:
        verbose_name = 'slide picture'
        verbose_name_plural = 'slide pictures'
        db_table = 'd_slide'
