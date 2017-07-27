# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ['products']
    list_display = ['id', 'create_date', 'username', 'full_price']
    list_filter = ['create_date', 'username']
    search_fields = ['id', 'create_date']

admin.site.register(Order, OrderAdmin)
