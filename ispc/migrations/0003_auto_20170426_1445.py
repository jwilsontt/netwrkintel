# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ispc', '0002_auto_20170426_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ispointcodes',
            name='dec',
            field=models.IntegerField(default=1),
        ),
    ]