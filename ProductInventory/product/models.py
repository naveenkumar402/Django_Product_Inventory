from django.db import models
from customer.models import Customer
# Create your models here.
class Products(models.Model):
    product_name=models.TextField()
    price=models.IntegerField()
    category=models.TextField()
    email = models.ForeignKey(Customer, to_field='email', on_delete=models.CASCADE)
    

