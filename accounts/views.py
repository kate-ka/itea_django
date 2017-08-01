# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import User
from .forms import *


class UsersView(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['users'] = User.get_all_users()
        return context


class UserRegisterView(TemplateView):
    template_name = "registration.html"

    def registration(self, request):
        form = UserRegisterForm()
        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
        else:
            form = UserRegisterForm()
        return render(request, 'templates/registration.html', {'form': form})


class UserLoginView(TemplateView):
    template_name = "login.html"

    def login(self, request):
        form = UserLoginForm()
        return render(request, 'templates/login.html', {'form': form})