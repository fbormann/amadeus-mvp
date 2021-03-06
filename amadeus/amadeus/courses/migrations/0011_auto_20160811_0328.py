# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-11 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20160729_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='course',
            name='goals',
            field=models.TextField(blank=True, verbose_name='Objectives'),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_approved',
            field=models.BooleanField(default=False, verbose_name='approved'),
        ),
        migrations.AlterField(
            model_name='course',
            name='limit',
            field=models.IntegerField(default=0, verbose_name='Student_Limits'),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='programa',
            field=models.TextField(blank=True, verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='slug',
            field=models.SlugField(verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='module',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='module',
            name='slug',
            field=models.SlugField(max_length=100, verbose_name='Identifier'),
        ),
        migrations.AlterField(
            model_name='module',
            name='visible',
            field=models.BooleanField(default=False, verbose_name='Visible'),
        ),
    ]
