# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20170320_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='product/static/product/'),
        ),
    ]
