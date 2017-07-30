# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Cart


class CartView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['carts'] = Cart.objects.all()
        context['user'] = self.request.user
        context['products'] = Cart.get_all_products()
        return context