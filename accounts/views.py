# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import User


class UsersView(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context

    @staticmethod
    def user_list(self, request):
        return render(request, 'apps/accounts/users.html', {})