from django.conf.urls import url

from .views import OrderView

urlpatterns = [
    url(r'^orders/$', OrderView.as_view(), name="orders")
]