# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.http import HttpResponse, HttpResponseNotFound


class User(AbstractUser):

    GENDER_CHOICES = (('unknown', 'unknown'), ('male', "male"), ('female', "female"))

    # def default_username(user):
    #     return 'user#{}'.format(user.id)

    # FIXME Sasha Shmigelskii: create write default name look like "user#1, user#2, etc.
    # username = models.CharField(max_length=50, unique=True)
    password = models.CharField(default='00', max_length=256, blank=True)
    mobile_number = models.CharField(max_length=13, blank=True)  # +380671111111 - 13 signs
    home_address = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to='accounts/photo',
                              height_field=120,
                              width_field=160,
                              blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='')

    class Meta:
        ordering = ['id']
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __unicode__(self):
        return '{}#{}'.format(self.username, self.id)

    @staticmethod
    def get_all_users():
        return User.objects.all()

    @staticmethod
    def get_user_by_name(name):
        return User.objects.filter(name=name).first()

    @staticmethod
    def current_datetime(request):
        now = datetime.datetime.now()
        html = "<html><body>It is now %s.</body></html>" % now
        return HttpResponse(html)

    def deactivation_user(self):
        self.is_active=False
        self.save()
