# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-24 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0037_auto_20180122_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
