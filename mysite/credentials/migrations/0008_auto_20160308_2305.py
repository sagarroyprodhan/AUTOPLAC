# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0007_auto_20160308_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='permanent_address',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
