# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20160724_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
    ]
