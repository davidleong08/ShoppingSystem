from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    photo = models.CharField('user_avatar', max_length=5000)
    level = models.CharField('user_level', max_length=1)

    def __str__(self):
        return self.username

