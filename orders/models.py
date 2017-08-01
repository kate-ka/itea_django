# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from accounts.models import User
from django.db import models
from django.conf import settings
from carts.models import Cart
from core.models import BaseModel
from coupons.models import ItemSaleCoupon
from products.models import Product


class Order(BaseModel):

    class Meta:
        ordering = ['-id']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    cart = models.ForeignKey(Cart)
    products = models.ManyToManyField(Product)
    username = models.ForeignKey(User)
    coupon = models.ForeignKey(ItemSaleCoupon, null=True, blank=True,
                               verbose_name="Coupon")
    additional_information = models.TextField(
        max_length=450, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    full_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Full price")
    created_date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField()
    payment_cash = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.id)
