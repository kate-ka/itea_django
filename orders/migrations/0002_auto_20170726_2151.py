# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='username',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='carts.Cart'),
            preserve_default=False,
        ),
    ]