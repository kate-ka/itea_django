# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('additional_information', models.TextField(max_length=450, null=True, blank=True)),
                ('quantity', models.PositiveIntegerField(null=True, blank=True)),
                ('full_price', models.DecimalField(verbose_name='Full price', max_digits=10, decimal_places=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('sent_date', models.DateTimeField()),
                ('payment_cash', models.BooleanField(default=True)),
                ('coupon', models.ForeignKey(verbose_name='Coupon', blank=True, to='coupons.ItemSaleCoupon', null=True)),
                ('products', models.ManyToManyField(to='products.Product')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-full_price'],
            },
        ),
    ]
