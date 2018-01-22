# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0036_auto_20180121_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='drink',
            name='url_height',
            field=models.PositiveIntegerField(default=200, editable=False),
        ),
        migrations.AlterField(
            model_name='drink',
            name='url_width',
            field=models.PositiveIntegerField(default=200, editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]