from django.db import models

# Create your models here.
class Customer(models.Model):
    fullname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    Phone=models.IntegerField()
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)

