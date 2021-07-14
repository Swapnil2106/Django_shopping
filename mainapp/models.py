from django.db import models

# Create your models here.
class Category(models.Model):
	cat=models.CharField(max_length=100,default=None)
	def __str__(self):
		return self.cat

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=8, decimal_places=2,default=0)
	img = models.ImageField(upload_to='pics',null=True,blank=True,height_field=None, width_field=None)
	cat = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)
	def __str__(self):
		return self.name


class CustomerModel(models.Model):
    userid = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=10)


class OrderModel(models.Model):
    username = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=10)
    address = models.TextField()
    orderitems = models.CharField(max_length=100)
    status = models.CharField(max_length=100)