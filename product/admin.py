from django.contrib import admin
<<<<<<< HEAD
from .models import Product, Size, Image
=======
from .models import Product, Size
>>>>>>> origin/master
# Register your models here.

class SizeAdmin(admin.TabularInline):
    model = Size
    extra = 1

<<<<<<< HEAD
class ImageAdmin(admin.TabularInline):
    model = Image
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin, SizeAdmin]
=======
class ProductAdmin(admin.ModelAdmin):
    inlines = [SizeAdmin]
>>>>>>> origin/master
    list_display = ('type', 'manufacturer', 'name', 'cost', 'new', 'sells')
    list_filter = ['type']

admin.site.register(Product, ProductAdmin)