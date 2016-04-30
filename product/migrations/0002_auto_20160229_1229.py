# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='craft',
            options={'verbose_name_plural': 'Crafts'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='craft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Craft'),
        ),
    ]
