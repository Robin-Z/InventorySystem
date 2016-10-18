
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^accounts/login/$', login),    # Django build-in login view
    url(r'^accounts/logout/$', logout, {'next_page': '/inventory_module/accounts/login'}, name='logout'),
    url(r'^inventory_page/$', views.inventory, name='inventory'),
    url(r'^my_borrow_list/$', views.my_borrow, name='my_borrow_list'),
    url(r'^my_info/$', views.my_info, name='my_info'),
    url(r'^borrow_material/(\d+)/$', views.borrow_material, name='borrow_material'),
    url(r'^add_borrow_record/$', views.add_borrow_record, name='add_borrow_record'),

]
