# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

# Register your models here.

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name',
                    'mobile_number', 'is_active', 'is_staff']
    list_filter = ['username']
    search_fields = ['username', 'email']

    
admin.site.register(User, UserAdmin)
