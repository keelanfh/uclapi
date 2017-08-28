# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 16:26
from __future__ import unicode_literals

import dashboard.app_helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_app_scope'),
        ('dashboard', '0008_auto_20170701_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='client_id',
            field=models.CharField(
                default=dashboard.app_helpers.generate_app_client_id,
                max_length=33,
                unique=True
            ),
        ),
        migrations.AlterField(
            model_name='app',
            name='client_secret',
            field=models.CharField(
                default=dashboard.app_helpers.generate_app_client_secret,
                max_length=64,
                unique=True
            ),  
        ),
    ]
