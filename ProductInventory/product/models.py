from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.TextField()
    price=models.IntegerField()
    category=models.TextField()
    email=models.EmailField()
    mrp=models.IntegerField(default=0)