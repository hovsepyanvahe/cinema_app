# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-05 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181203_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=6, null=True),
        ),
    ]
