from django.db import models

# Create your models here.
	


def _str_(self):
	return self.title

class Banner(models.Model):
	image=models.ImageField(upload_to='add_banner/')

class Animation(models.Model):
	image=models.ImageField(upload_to='Animation/')
	
class Product(models.Model):
	pname=models.CharField(max_length=255)
	price=models.IntegerField()
	pcolor=models.CharField(default='red',max_length=20)
	image=models.ImageField(upload_to='add_product/')
	
	
