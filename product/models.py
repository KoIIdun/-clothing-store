from django.db import models
from django import forms
import django_filters
from django import forms


# Create your models here.

                     
STATUS_CHOICES = (
    (0, 'Puma'),
    (1, 'Adidas'),
    (2, 'Nike'),
)

class Product(models.Model):
    type = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    name = models.CharField(max_length=200)
    index = models.CharField(max_length=20)
    cost = models.IntegerField()                      
    colors = models.TextField(max_length=20)
    year = models.IntegerField()
    sells = models.BooleanField(default=False)
    new = models.BooleanField(default=False)

class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=4)
    count = models.IntegerField()

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to= 'media')
                     
class ProductFilter(django_filters.FilterSet):                         
    status = django_filters.MultipleChoiceFilter(choices=STATUS_CHOICES,  widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Product
        fields = ['status', 'name']
