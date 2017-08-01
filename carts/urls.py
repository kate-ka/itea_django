from django.conf.urls import url

from .views import CartView, CartProductEdit, CartProductAdd, CartProductDeleteView

urlpatterns = [
    url(r'^cart_view/$', CartView.as_view(), name="cart_view"),
    url(r'^cart_edit/$', CartProductEdit.as_view(), name='cart_edit'),
    url(r'^cart_add/$', CartProductAdd.as_view(), name='cart_add'),
    url(r'^cart_view/delete/$', CartProductDeleteView.as_view(), name='cart_product_delete')
]
