from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^users/$', UsersView.as_view(), name="users"),
    url(r'^registration/$', UserRegisterView.as_view(), name='registration'),
    url(r'^login/$', UserLoginView.as_view(), name='login'),
]