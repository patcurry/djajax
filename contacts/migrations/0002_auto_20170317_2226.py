# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.CharField(max_length=24, unique=True),
        ),
    ]
