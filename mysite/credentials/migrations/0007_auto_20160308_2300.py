# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0006_auto_20160308_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
