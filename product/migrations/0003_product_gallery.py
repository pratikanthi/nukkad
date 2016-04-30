# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        ('product', '0002_auto_20160229_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gallery',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_gallery', to='photologue.Gallery'),
        ),
    ]
