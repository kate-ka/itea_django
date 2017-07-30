# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('place_order', models.BooleanField(default=False, verbose_name='Place Order')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
                ('unit_price', models.DecimalField(verbose_name='Unit Price', max_digits=50, decimal_places=2)),
                ('shipping_cost', models.DecimalField(verbose_name='Shipping Cost', max_digits=50, decimal_places=2)),
                ('tax_cost', models.DecimalField(verbose_name='TAX', max_digits=50, decimal_places=2)),
                ('subtotal_amount', models.DecimalField(verbose_name='Subtotal', max_digits=50, decimal_places=2)),
                ('products', models.ManyToManyField(related_name='products', to='products.Product')),
            ],
            options={
                'ordering': ['create_date'],
                'verbose_name': 'Cart',
            },
        ),
    ]
