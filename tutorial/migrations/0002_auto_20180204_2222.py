# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-04 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cityid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.City')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='countryid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.Country'),
        ),
    ]