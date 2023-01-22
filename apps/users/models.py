from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
    user_img = models.ImageField('user_avatar', upload_to='userImage')
    level = models.CharField('user_level', max_length=1, default=1)

    def __str__(self):
        return self.username

