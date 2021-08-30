from django.db import models
from django.db.models.base import Model

# Create your models here.
class customer(models.Model):
    email=models.EmailField()
    name=models.TextField(max_length=20)
    address=models.TextField(max_length=20)
    address2=models.TextField(max_length=20)
    city=models.TextField(max_length=20)
    state=models.TextField(max_length=20)
    password=models.TextField(max_length=20)