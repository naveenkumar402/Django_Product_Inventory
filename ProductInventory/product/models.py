from django.db import models

# Create your models here.
class Products(models.Model):
    product_name=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.TextField()
    email=models.EmailField()