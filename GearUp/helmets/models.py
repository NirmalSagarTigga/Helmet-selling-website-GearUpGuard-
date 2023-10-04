from django.db import models

# Create your models here.
from admin_dashboard.models import *

class Customer(models.Model):
    fullname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    Phone=models.IntegerField()
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)

class Cart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    register=models.ForeignKey(Customer,on_delete=models.CASCADE)
    qnty=models.IntegerField()
	
