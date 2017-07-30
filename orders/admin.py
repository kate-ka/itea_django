# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ['products']

admin.site.register(Order, OrderAdmin)
