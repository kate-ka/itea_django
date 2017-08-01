from django.conf.urls import url

from .views import OrderView, OrderDetailsView

urlpatterns = [
    url(r'^orders/$', OrderView.as_view(), name="orders"),
    url(r'^order_detail/?/order_id=(?P<order_id>\d+)/$',
        OrderDetailsView.as_view(),
        name="order_details")
]