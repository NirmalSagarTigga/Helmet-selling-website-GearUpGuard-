from django.db import models

# Create your models here.
	
class Banner(models.Model):
	image=models.ImageField(upload_to='banner/')

class Animation(models.Model):
	image=models.ImageField(upload_to='Animation/')
	
class Product(models.Model):
	pname=models.CharField(max_length=255)
	price=models.IntegerField()
	image=models.ImageField(upload_to='product/')
	
	
