# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Order


class OrderView(TemplateView):
    template_name = 'orders.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.all()
        context['orders_count'] = len(Order.objects.all())
        return context


class OrderDetailsView(TemplateView):
    context_object_name = 'order'
    template_name = 'order_details.html'

    def get_context_data(self, **kwargs):
        context = super(OrderDetailsView, self).get_context_data(**kwargs)
        order = Order.objects.get(id=kwargs.get('order_id'))
        context['order'] = order
        context['products'] = order.products.all()
        return context
