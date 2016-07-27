# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 23:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20160724_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='course',
            name='subscription_finish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
