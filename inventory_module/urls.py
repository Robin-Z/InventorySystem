
from django.conf.urls import url

from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^accounts/login/$', login),    # Django build-in login view
    url(r'^inventory_page/$', views.inventory, name='inventory'),

    url(r'^my_borrow_list/$', views.my_borrow, name='my_borrow_list'),
    url(r'^borrow_material/(\d+)/$', views.borrow_material, name='borrow_material'),
    #url(r'^borrow_material/$', views.borrow_material, name='borrow_material'),
]
