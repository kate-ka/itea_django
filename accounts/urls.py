from django.conf.urls import url

from .views import UsersView

urlpatterns = [
    url(r'^users/$', UsersView.as_view(), name="users")
]