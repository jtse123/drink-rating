# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0012_auto_20171207_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]