# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import User
from .forms import *
import requests


class UsersView(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['users'] = User.get_all_users()
        return context


class UserRegisterView(TemplateView):
    template_name = "registration.html"

    def registration(self, **kwargs):
        form = RegisterForm()
        return render(requests, 'templates/registration.html', {'form': form})


class UserLoginView(TemplateView):
    template_name = "login.html"

    def login(self, **kwargs):
        form = LoginForm()
        return render(requests, 'templates/login.html', {'form': form})