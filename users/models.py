from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.

class Customers(models.Model):
    custName = models.CharField(max_length=100)
    custFirstName = models.CharField(max_length=100,default='Test')
    custLastName = models.CharField(max_length=100,default='Test')
    custAddr = models.TextField()
    custPhone = models.IntegerField(default=1234567890)
    custEmail = models.EmailField(default='abc@gmail.com')
    objects = UserManager()