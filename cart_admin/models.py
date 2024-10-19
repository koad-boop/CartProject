from django.db import models
from cart.models import Customer

# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    
class Category(models.Model):
    name=models.CharField(max_length=50)
    des=models.CharField(max_length=100)

def __str__(self):
    return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    des=models.CharField(max_length=100)
    image=models.FileField(upload_to='uploads/products/')


class Cart(models.Model):
    pro_id = models.ForeignKey(Product,on_delete=models.CASCADE,null='TRUE')
    cust_id = models.ForeignKey(Customer,on_delete=models.CASCADE,null='TRUE')
    quantity = models.IntegerField(default=1)
    
    

