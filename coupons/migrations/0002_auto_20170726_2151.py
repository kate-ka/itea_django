# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcoupon',
            name='coupon_secret',
            field=models.CharField(default=b'4be8e951c6f248f9831c29e925d3417d', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='salecoupon',
            name='coupon_secret',
            field=models.CharField(default=b'4be8e951c6f248f9831c29e925d3417d', editable=False, max_length=64),
        ),
    ]
