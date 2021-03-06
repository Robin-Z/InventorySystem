from django import forms
from django.contrib.auth.forms import AuthenticationForm


"""
Customized build-in login form in LoginForm, otherwise you cannot use Bootstrap CSS.
"""


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'name': 'username',
                                                             'placeholder': 'User name'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'name': 'password',
                                                                 'placeholder': 'Passowrd'}))


"""
Customized borrow material form
"""


class borrow_material_form(forms.Form):
    goods_id = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
    goods_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
    goods_part_num = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
    goods_spec = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
    goods_revision = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
    goods_location = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
    goods_unit = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
    goods_onhand_qty = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'readonly': 'readonly',
                                                                                     'class': 'input-lg'}))
    goods_borrow_qty = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'input-lg'}))
    goods_borrow_date = forms.DateField(widget=forms.DateInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))


"""
Use Django form to customize my info form
"""


class my_info_form(forms.Form):
    user_id = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'readonly': 'readonly',
                                                                            'class': 'input-lg'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly',
                                                              'class': 'input-lg'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'class': 'input-lg'}))
