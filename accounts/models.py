# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    GENDER_CHOICES = (('UN', 'unknown'), ('MA', "male"), ('FE', "female"))

    mobile_number = models.CharField(max_length=20, blank=True)
    home_address = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='accounts/photo', blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='')

    class Meta:
        ordering = ['id']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)
