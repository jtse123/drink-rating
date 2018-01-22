# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-22 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0035_auto_20180121_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='drink',
            name='width_field',
        ),
        migrations.AddField(
            model_name='drink',
            name='url_height',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AddField(
            model_name='drink',
            name='url_width',
            field=models.PositiveIntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='drink',
            name='image',
            field=models.ImageField(blank=True, height_field='url_height', null=True, upload_to='', width_field='url_width'),
        ),
    ]
