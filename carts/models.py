# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from core.models import BaseModel
from orders.models import Order
from products.models import Product

   
class Cart(BaseModel):

    # Cart Model
    
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
      
    # place_order = models.BooleanField(default=False, verbose_name=_('Place Order'))
     
    products = models.ManyToManyField(Product, related_name='products')
      
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
     
    unit_price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Unit Price"))
   
    # Ось це гуд
    shipping_costs = models.ManyToManyField("ShippingCost", 
        related_name="shipping_costs", verbose_name=_("Shipping Cost"))
    tax_cost = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("TAX"))
    subtotal_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Subtotal"))

    class Meta(object):
        verbose_name = _("Cart")
        ordering = ['create_date']

    @staticmethod
    def get_all_products():
        return Product.objects.all()


class ShippingCost(models.Model):

    shipping_name = models.CharField(max_length=250, blank=True, null=True)
    value = models.DecimalField(max_digits=50, decimal_places=2)

