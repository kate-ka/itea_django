# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0004_auto_20170718_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcoupon',
            name='coupon_secret',
            field=models.CharField(default=b'675596032fa743c4b22773c68f3ff4bb', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='salecoupon',
            name='coupon_secret',
            field=models.CharField(default=b'675596032fa743c4b22773c68f3ff4bb', editable=False, max_length=64),
        ),
    ]
