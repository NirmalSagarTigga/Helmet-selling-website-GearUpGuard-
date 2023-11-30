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
    
	
class Order(models.Model):
    
    fname=models.CharField(max_length=150,null=False)
    email=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    zip=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=150,null=True)
    ordersstatus=(
        ('pending', 'pending'),
         ('out for shipping', 'out for shipping'),
         ('completed','completed'),
    )
    status=models.CharField(max_length=150,choices=ordersstatus, default='completed')
    message=models.TextField(null=True)
                            
class OrderItem(models.Model):
   
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField(null=False)