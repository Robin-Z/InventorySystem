from django.db import models

# Create your models here.


# Role-based access control Models
class func_modules(models.Model):
    func_modules_id = models.IntegerField()
    func_modules_name = models.CharField(max_length=20)

    def __unicode__(self):
        return u'Func_module: %s' % self.func_modules_name

class role(models.Model):
    role_id = models.CharField(max_length=10)
    role_name = models.CharField(max_length=20)
    role_func_modules = models.ManyToManyField(func_modules)

    def __unicode__(self):
        return u'Role: %s' % self.role_name

# User Models Definition
class department(models.Model):
    department_id = models.CharField(max_length=10)
    department_name = models.CharField(max_length=20)

    def __unicode__(self):
        return u'Department: %s' % self.department_name

class employee(models.Model):
    employee_id = models.CharField(max_length=20)
    employee_name = models.CharField(max_length=20)
    employee_email = models.CharField(max_length=50)
    employee_department = models.ForeignKey(department)

    def __unicode__(self):
        return u'Employee: %s, %s' % (self.employee_id, self.employee_name)

class user(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    user_passwd = models.CharField(max_length=20)
    user_employee = models.ForeignKey(employee)
    user_role = models.ForeignKey(role)

    def __unicode__(self):
        return u'User: %s, %s' % (self.user_id, self.user_name)

# Vendor Model definition
class vendor(models.Model):
    vendor_id = models.CharField(max_length=10)
    vendor_name = models.CharField(max_length=30)
    vendor_country = models.CharField(max_length=20)
    website_url = models.URLField()

    def __unicode__(self):
        return u'Vendor: %s' % self.vendor_name

# Goods category model definition
class category(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=20)

    def __unicode__(self):
        return u'Category: %s' % self.category_name

# Goods inventory model definition
class inventory(models.Model):
    inventory_id = models.IntegerField()
    inventory_name = models.CharField(max_length=20)
    inventory_location = models.CharField(max_length=30)

    def __unicode__(self):
        return u'Inventory: %s, %s' % (self.inventory_name, self.inventory_location)

# Goods model definition
class goods(models.Model):
    goods_name = models.CharField(max_length=30)
    goods_part_num = models.CharField(max_length=30)
    goods_spec = models.CharField(max_length=50)
    goods_revision = models.CharField(max_length=50)
    goods_qty = models.IntegerField()
    goods_unit = models.CharField(max_length=10, null=True)
    goods_status = models.CharField(max_length=10, null=True)
    goods_location = models.CharField(max_length=200)
    remark = models.CharField(max_length=200)
    create_date = models.DateField()
    update_date = models.DateField()
    goods_category = models.ForeignKey(category)
    goods_vendor = models.ForeignKey(vendor)
    goods_inventory = models.ForeignKey(inventory)
    goods_user = models.ForeignKey(user, related_name='user_goods_creator')

    def __unicode__(self):
        return u'Goods: %s, %s' % (self.goods_name, self.goods_location)


#Borrower who borrow goods from inventory

class borrow_goods_list(models.Model):
    borrower = models.ForeignKey(user,related_name='borrower_in_user')
    borrow_goods = models.ForeignKey(goods)
    borrow_goods_qty = models.IntegerField()
    borrow_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    borrow_status = models.CharField(max_length=10, default='Open')

    def __unicode__(self):
        return u'Borrower: %s' % (self.borrower)
