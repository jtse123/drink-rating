# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-09 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0028_auto_20180109_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='image',
            field=models.ImageField(blank=True, height_field='height', null=True, upload_to='', width_field='width'),
        ),
    ]
