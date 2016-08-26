
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^access_filter/$', views.access_filter, name='access_filter'),
    url(r'^inventory_page/$', views.inventory, name='inventory'),
]
