# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0009_auto_20171204_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='drink_id',
        ),
        migrations.AddField(
            model_name='rating',
            name='drink_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='drinkproj.Drink'),
            preserve_default=False,
        ),
    ]
