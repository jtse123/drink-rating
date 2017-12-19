# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 18:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0008_drink_event_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_Lineup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkproj.Drink')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkproj.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='rating',
            name='drink_id',
        ),
    ]