# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 02:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0018_auto_20171210_1831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='drink_id',
            new_name='drink',
        ),
    ]
