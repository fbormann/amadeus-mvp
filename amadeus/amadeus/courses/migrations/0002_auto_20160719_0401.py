# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 04:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.AddField(
            model_name='course',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='course',
            name='goals',
            field=models.TextField(blank=True, verbose_name='Objetivos'),
        ),
        migrations.AddField(
            model_name='course',
            name='limit',
            field=models.IntegerField(default=0, verbose_name='Limite_Alunos'),
        ),
        migrations.AddField(
            model_name='course',
            name='programa',
            field=models.TextField(blank=True, verbose_name='Programa'),
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
        migrations.AddField(
            model_name='course',
            name='subscription_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
