# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='category/images')

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Product(BaseModel):
    parent = models.ForeignKey("self", related_name="children", null=True, blank=True)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    brand = models.ForeignKey(Brand, related_name="brand_products")
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='category_products')
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    attribute_values = models.ManyToManyField("AttributeValue", related_name="attribute_values")

    class Meta:
        ordering = ['-create_date']

    def __unicode__(self):
        return self.name

    def product_view(self):
        image = ProductImage.objects.filter(product=self).first()
        return u'<img src="%s" width="80px"/>' % image.image.url if image else ""
    product_view.short_description = 'Image'
    product_view.allow_tags = True


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, related_name='product_images')
    image = models.ImageField(upload_to='products/images')
    caption = models.CharField(max_length=200, blank=True)


class AttributeValue(models.Model):
    """
    AttributeValue contains value of a specified AttributeName.
    For ex if AttributeName is 'display diagonal' value can be 13".
    Relation between Product and AttributeValues is MtM.
    """

    attribute_name = models.ForeignKey("AttributeName", related_name="attribute_values")
    value = models.CharField(max_length=250)

    def __unicode__(self):
        return "{} - {} - {}".format(self.attribute_name.category.name, self.attribute_name.name, self.value)


class AttributeName(models.Model):
    """
    AttributeName is a name of Product attribute,
    like 'display diagonal', 'ram', 'processor' etc.
    It's also connected with Product category, as some attributes'
    names are suitable for ex. only for notebooks but not for chairs.
    """
    name = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey("Category", related_name="category_attributes")

    def __unicode__(self):
        return self.name


class ProductReview(BaseModel):
    RATINGS = ((5, 5), (4, 4), (3, 3), (2, 2), (1, 1),)

    product = models.ForeignKey("Product", related_name="product_reviews")
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_reviews")
    rating = models.PositiveSmallIntegerField(default=0, choices=RATINGS)