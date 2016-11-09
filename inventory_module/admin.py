from django.contrib import admin
from inventory_module.models import vendor, category, inventory, goods, borrow_goods_list

# Register your models here.
admin.site.register(vendor)
admin.site.register(category)
admin.site.register(inventory)
admin.site.register(goods)
admin.site.register(borrow_goods_list)
