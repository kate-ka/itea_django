# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls.base import reverse

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

    def sorted_category_products(self, sort_by):
        return self.category_products.order_by(sort_by)

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"category_slug": self.slug})


class Brand(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    def sorted_brand_products(self, sort_by):
        return self.brand_products.order_by(sort_by)

    def get_absolute_url(self):
        return reverse("brand_detail", kwargs={"brand_id": self.id})


class Product(BaseModel):
    parent = models.ForeignKey("self", related_name="children", null=True, blank=True)
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=255)
    brand = models.ForeignKey(Brand, related_name="brand_products")
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    currency = models.ForeignKey("Currency")
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='category_products')
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    attribute_values = models.ManyToManyField("AttributeValue", related_name="attribute_values")
    rating = models.FloatField(default=0)

    class Meta:
        ordering = ['-create_date']

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def product_view(self):
        image = ProductImage.objects.filter(product=self).first()
        return u'<img src="%s" width="80px"/>' % image.image.url if image else ""
    product_view.short_description = 'Image'
    product_view.allow_tags = True

    def product_price(self):
        default_currency = Currency.objects.filter(is_default=True).first()
        if default_currency and default_currency != self.currency:
            current_coefficient = default_currency.coefficient / self.currency.coefficient
            return '{} {}'.format(round(self.price * current_coefficient, 2), default_currency.symbol)
        return '{} {}'.format(self.price, self.currency.symbol)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"product_slug": self.slug})

    def get_product_reviews(self):
        return self.product_reviews.all()


class Currency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    coefficient = models.DecimalField(default=0.00, max_digits=9, decimal_places=4,
                                      verbose_name="Ratio to the dollar")
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Currency'

    def __str__(self):
        return "{} {} - {}, {}".format(self.symbol, self.code, self.name, self.is_default)

    def save(self, *args, **kwargs):
        if self.is_default:
            Currency.objects.filter(is_default=True).update(is_default=False)
        super(Currency, self).save(*args, **kwargs)


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