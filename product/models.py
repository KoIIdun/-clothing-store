from django.db import models
from django import forms

# Create your models here.

class Product(models.Model):
    type = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    cost = models.IntegerField()
    description = models.TextField(max_length=200)
    sells = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.IntegerField()
    count = models.IntegerField()

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()