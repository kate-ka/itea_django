# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0007_auto_20170720_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftcoupon',
            name='coupon_secret',
            field=models.CharField(default=b'b313f6c5cc6b4e4593954a065ff3849b', editable=False, max_length=64),
        ),
        migrations.AlterField(
            model_name='salecoupon',
            name='coupon_secret',
            field=models.CharField(default=b'b313f6c5cc6b4e4593954a065ff3849b', editable=False, max_length=64),
        ),
    ]
