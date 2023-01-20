from django.db import models
from apps.users.models import MyUser
from apps.goods.models import ProductsCategory, Product


# Create your models here.


class Order(models.Model):
    purchase_order_number = models.IntegerField(primary_key=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    total_order_amount = models.IntegerField()
    status_choice = (
        (0, "pending"),
        (1, "hold"),
        (2, "shipped"),
        (3, "cancelled"),
    )
    purchase_order_status = models.CharField(max_length=1200, choices=status_choice)
    customer = models.OneToOneField(MyUser, on_delete=models.DO_NOTHING)
    shipped_date = models.DateTimeField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.purchase_order_number)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'd_order'


class ShoppingCart(models.Model):
    shopping_cart_id = models.IntegerField(primary_key=True)
    purchase_order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(ProductsCategory, on_delete=models.DO_NOTHING)
    count_number = models.IntegerField()
    total_price = models.DecimalField(max_digits=32, decimal_places=8)

    def __str__(self):
        return str(self.shopping_cart_id)

    class Meta:
        verbose_name = 'shopping cart'
        db_table = 'd_shoppingcart'
