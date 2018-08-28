from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, default='')
    address = models.TextField(default='')
    def __str__(self):
        return self.username
class Consignee(models.Model):
    consignee = models.CharField(max_length=20, default='')
    detail_add = models.TextField(default='')
    phone = models.CharField(max_length=11, default='')
    postcode = models.CharField(max_length=8, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.consignee
class ShopType(models.Model):
    name = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.name
class Goods(models.Model):
    name = models.CharField(max_length=20, default='')
    pictures = models.ImageField(upload_to='goodsPictures', default='')
    price = models.FloatField(default='')
    unit = models.CharField(max_length=30, default='')
    goods_click = models.IntegerField(default='')
    intro = models.TextField(default='')
    repertory = models.IntegerField(default='')
    comment = models.TextField(default='')
    type = models.ForeignKey(ShopType, on_delete=models.CASCADE, default='')
    def __str__(self):
        return self.name