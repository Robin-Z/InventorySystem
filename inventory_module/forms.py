from django import forms
from django.contrib.auth.forms import AuthenticationForm

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'User name'}))
    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Passowrd'}))

class borrow_material_form(forms.Form):
    goods_id = forms.IntegerField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_part_num = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_spec = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_revision = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_location = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_unit = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_onhand_qty = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    goods_borrow_qty = forms.IntegerField(min_value=0)
    goods_borrow_date = forms.DateField(widget=forms.DateInput(attrs={'readonly': 'readonly'}))

class my_info_form(forms.Form):
    user_id = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'readonly': 'readonly', 'outline': 'medium'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'outline': 'medium'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly', 'outline': 'medium'}))
