# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0023_auto_20171210_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]