
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from .forms import LoginForm

urlpatterns = [
    # Django build-in login view
    url(r'^accounts/login/$', login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}),
    url(r'^accounts/logout/$', logout, {'next_page': '/inventory_module/accounts/login'}, name='logout'),
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^inventory_page/$', views.inventory, name='inventory'),
    url(r'^my_borrow_list/$', views.my_borrow, name='my_borrow_list'),
    url(r'^my_info/$', views.my_info, name='my_info'),
    url(r'^borrow_material/(\d+)/$', views.borrow_material, name='borrow_material'),
    url(r'^add_borrow_record/$', views.add_borrow_record, name='add_borrow_record'),
    url(r'^query_by_keyword/$', views.query_by_keyword, name='query_by_keyword'),
    url(r'^about/$', views.about_page, name='about_page'),
    url(r'^contact/$', views.contact_page, name='contact_page'),
]
