from django import forms

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
    user_id = forms.IntegerField(min_value=0, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
