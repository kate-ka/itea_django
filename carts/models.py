# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from core.models import BaseModel
from orders.models import Order
from products.models import Product

   
class Cart(BaseModel):
     # для чього це поле? - щоб мати флажок чи в карті натиснута кнопка - прийняти замовлення чи ні
    place_order = models.BooleanField(default=False, verbose_name=_('Place Order'))

    # Поле продукт, але продуктів може бути багато, краще робити продуктс
    products = models.ManyToManyField(Product, related_name='products')
      
    # кількість чього? - к-сть одного продукту в кошику
    quantity = models.PositiveIntegerField(verbose_name=_("Quantity"))
     
    # Не зрозуміло що ми тут будемо зберігати? - ціна продукту з к-стю 1
    unit_price = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Unit Price"))
   
    # Ось це гуд
    shipping_cost = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Shipping Cost"))
    tax_cost = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("TAX"))
    subtotal_amount = models.DecimalField(max_digits=50, decimal_places=2, verbose_name=_("Subtotal"))

    class Meta(object):
        verbose_name = _("Cart")
        ordering = ['create_date']
