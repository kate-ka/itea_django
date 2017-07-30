# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCoupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('coupon_secret', models.CharField(default=b'f69f0abca3d049098f5736149740221b', max_length=64, editable=False)),
                ('is_valid', models.BooleanField(default=True)),
                ('value_type', models.CharField(default=b'N', max_length=1, editable=False, choices=[(b'P', b'percent'), (b'N', b'natural')])),
                ('git_type', models.CharField(max_length=1, editable=False, choices=[(b'P', b'personal_gift'), (b'M', b'mass_gift')])),
                ('value', models.PositiveIntegerField()),
                ('expired_date', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999))),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PromoGiftCoupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_used', models.PositiveIntegerField()),
                ('GiftCoupon', models.OneToOneField(editable=False, to='coupons.GiftCoupon')),
            ],
            options={
                'db_table': 'gift_promo',
            },
        ),
        migrations.CreateModel(
            name='SaleCoupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
                ('coupon_secret', models.CharField(default=b'f69f0abca3d049098f5736149740221b', max_length=64, editable=False)),
                ('is_valid', models.BooleanField(default=True)),
                ('value_type', models.CharField(default=b'P', max_length=1, choices=[(b'P', b'percent'), (b'N', b'natural')])),
                ('sale_type', models.CharField(max_length=1, choices=[(b'I', b'Item sale'), (b'C', b'category_sale')])),
                ('default_value', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField()),
                ('expired_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGiftCoupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('used_date', models.DateTimeField(blank=True)),
                ('GiftCoupon', models.OneToOneField(editable=False, to='coupons.GiftCoupon')),
            ],
            options={
                'db_table': 'gift_user',
            },
        ),
        migrations.CreateModel(
            name='CategorySaleCoupon',
            fields=[
                ('salecoupon_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='coupons.SaleCoupon')),
                ('value', models.PositiveIntegerField(null=True, blank=True)),
                ('category', models.ForeignKey(related_name='category_coupon_related', to='products.Category')),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
            bases=('coupons.salecoupon',),
        ),
        migrations.CreateModel(
            name='ItemSaleCoupon',
            fields=[
                ('salecoupon_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='coupons.SaleCoupon')),
                ('value', models.PositiveIntegerField(null=True, blank=True)),
                ('product', models.ForeignKey(related_name='item_sale_product_related', to='products.Product')),
                ('sale_coupon', models.ForeignKey(related_name='item_sale_coupon_related', to='coupons.SaleCoupon')),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
            bases=('coupons.salecoupon',),
        ),
        migrations.AddField(
            model_name='categorysalecoupon',
            name='sale_coupon',
            field=models.ForeignKey(related_name='category_sale_coupon_related', to='coupons.SaleCoupon'),
        ),
    ]
