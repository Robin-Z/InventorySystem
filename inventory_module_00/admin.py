from django.contrib import admin
from inventory_module.models import func_modules, role, department, employee, user, vendor, category, inventory, goods, borrow_goods_list

# Register your models here.

admin.site.register(func_modules)
admin.site.register(role)
admin.site.register(department)
admin.site.register(employee)
admin.site.register(user)
admin.site.register(vendor)
admin.site.register(category)
admin.site.register(inventory)
admin.site.register(goods)
admin.site.register(borrow_goods_list)
