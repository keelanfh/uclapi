# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roombookings', '0006_bookinga_bookingb_lock'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinga',
            name='id',
            field=models.AutoField(default=999999999999, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingb',
            name='id',
            field=models.AutoField(default=999999999999, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookinga',
            name='slotid',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='bookingb',
            name='slotid',
            field=models.BigIntegerField(),
        ),
    ]
