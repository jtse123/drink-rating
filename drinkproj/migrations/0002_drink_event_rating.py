# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 03:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('drinkproj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('drink_name', models.CharField(max_length=200)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkproj.DrinkType')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkproj.Drink')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField()),
                ('comment', models.TextField()),
                ('post_date', models.DateTimeField(default=datetime.datetime(2017, 12, 4, 3, 0, 43, 501874, tzinfo=utc))),
                ('rating_choices', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=20)),
                ('drink_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinkproj.Drink')),
            ],
        ),
    ]
