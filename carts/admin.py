# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Cart, ShippingCost, Product


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'unit_price', 'quantity','tax_cost', 'subtotal_amount']


admin.site.register(Cart, CartAdmin)
admin.site.register(ShippingCost)
