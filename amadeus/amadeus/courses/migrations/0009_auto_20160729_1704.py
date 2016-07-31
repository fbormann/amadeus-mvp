# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20160729_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]