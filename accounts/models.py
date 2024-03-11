from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from datetime import datetime
from django.utils import timezone

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    product_favorites =models.ManyToManyField(Product)
    userphoto =models.ImageField(upload_to='imageprofile/%Y/%m/%d/')
    usershopphoto =models.ImageField(upload_to='imageshopprofile/%Y/%m/%d/')
    region=models.CharField(max_length=60)
    neighborhood=models.CharField(max_length=60)
    shopname=models.CharField(max_length=60) 
    shopaddress=models.CharField(max_length=120)
    zip_number=models.CharField(max_length=5)
    def __str__(self):
        return self.user.username
    