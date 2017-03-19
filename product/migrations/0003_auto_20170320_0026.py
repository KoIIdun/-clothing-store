# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='colors',
            field=models.TextField(default=12, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='index',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='size',
            name='size',
            field=models.CharField(max_length=4),
        ),
    ]
