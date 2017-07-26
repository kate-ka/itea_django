# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=250)),
                ('attribute_name', models.ForeignKey(related_name='attribute_values', to='products.AttributeName')),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='category/images')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=50, null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('price', models.DecimalField(default=0.0, max_digits=9, decimal_places=2, blank=True)),
                ('quantity', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('attribute_values', models.ManyToManyField(related_name='attribute_values', to='products.AttributeValue')),
                ('brand', models.ForeignKey(related_name='brand_products', to='products.Brand')),
                ('categories', models.ManyToManyField(related_name='category_products', to='products.Category')),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='products.Product', null=True)),
            ],
            options={
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='products/images')),
                ('caption', models.CharField(max_length=200, blank=True)),
                ('product', models.ForeignKey(related_name='product_images', default=None, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('delete_date', models.DateTimeField(db_index=True, null=True, blank=True)),
                ('text', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(default=0, choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)])),
                ('product', models.ForeignKey(related_name='product_reviews', to='products.Product')),
                ('user', models.ForeignKey(related_name='user_reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pk'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='attributename',
            name='category',
            field=models.ForeignKey(related_name='category_attributes', to='products.Category'),
        ),
    ]
