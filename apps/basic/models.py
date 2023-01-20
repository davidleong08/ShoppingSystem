from datetime import datetime

from django.db import models
from apps.users.models import MyUser


# Create your models here.


class ShippingAddress(models.Model):
    shipping_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=50)
    receiver_phone = models.IntegerField()
    receiver_mobile = models.IntegerField()
    receiver_province = models.TextField(max_length=100)
    receiver_city = models.CharField(max_length=100)
    receiver_district = models.CharField(max_length=100)
    receiver_address = models.TextField(max_length=100)
    receiver_zip = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.shipping_id) + self.receiver_name + str(self.receiver_phone)

    class Meta:
        verbose_name = "product information"
        verbose_name_plural = "product_information"
        db_table = 'd_shippingAddress'
