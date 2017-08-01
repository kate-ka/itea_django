# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DeleteView

from .models import Cart


class CartView(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['carts'] = Cart.objects.all()
        context['user'] = self.request.user
        context['products'] = Cart.get_all_products()
        return context

class CartProductEdit(TemplateView):
    template_name = "cart.html"

class CartProductAdd(TemplateView):
    template_name = "cart.html"

# class CartProductDeleteView(DeleteView):
#     template_name = "cart.html"

class CartProductDeleteView(DeleteView):
    model = Cart
    template_name = 'products_confirm_delete.html'

    def get_success_url(self):
        return reverse("cart_product_delete", kwargs={
            "delete_product_slug":self.kwargs['delete_product_slug']
        })