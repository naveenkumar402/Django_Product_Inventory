from typing import Any
from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(primary_key='true')
    mobile=models.BigIntegerField()
    state=models.TextField()
    country=models.TextField()

    