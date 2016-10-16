from django import forms

class borrow_material_form(forms.Form):
    goods_id = forms.IntegerField()
    goods_name = forms.CharField()
    goods_part_num = forms.CharField()
    goods_spec = forms.CharField()
    goods_revision = forms.CharField()
    goods_location = forms.CharField()
    goods_unit = forms.CharField()
    goods_onhand_qty = forms.IntegerField()
    goods_borrow_qty = forms.IntegerField()
    goods_borrow_date = forms.DateField()

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['goods_id'].widget.attrs['readonly'] = True
        self.fields['goods_name'].widget.attrs['readonly'] = True
        self.fields['goods_part_num'].widget.attrs['readonly'] = True
        self.fields['goods_spec'].widget.attrs['readonly'] = True
        self.fields['goods_revision'].widget.attrs['readonly'] = True
        self.fields['goods_location'].widget.attrs['readonly'] = True
        self.fields['goods_unit'].widget.attrs['readonly'] = True
        self.fields['goods_onhand_qty'].widget.attrs['readonly'] = True
        self.fields['goods_borrow_date'].widget.attrs['readonly'] = True


class my_info_form(forms.Form):
    user_id = forms.IntegerField()
    user_name = forms.CharField(max_length=254)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args,**kwargs)
        self.fields['user_id'].widget.attrs['readonly'] = True
        self.fields['user_name'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
