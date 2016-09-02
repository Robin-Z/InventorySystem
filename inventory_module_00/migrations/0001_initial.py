# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='borrowe_goods_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrow_goods_qty', models.IntegerField()),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField(blank=True)),
                ('borrow_status', models.CharField(default=b'Open', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_id', models.IntegerField()),
                ('category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_id', models.CharField(max_length=10)),
                ('department_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee_id', models.CharField(max_length=20)),
                ('employee_name', models.CharField(max_length=20)),
                ('employee_email', models.CharField(max_length=50)),
                ('employee_department', models.ForeignKey(to='inventory_module.department')),
            ],
        ),
        migrations.CreateModel(
            name='func_modules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('func_modules_id', models.IntegerField()),
                ('func_modules_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('goods_name', models.CharField(max_length=30)),
                ('goods_part_num', models.CharField(max_length=30)),
                ('goods_spec', models.CharField(max_length=50)),
                ('goods_revision', models.CharField(max_length=50)),
                ('goods_qty', models.IntegerField()),
                ('goods_unit', models.CharField(max_length=10, null=True)),
                ('goods_status', models.CharField(max_length=10, null=True)),
                ('goods_location', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('create_date', models.DateField()),
                ('update_date', models.DateField()),
                ('goods_category', models.ForeignKey(to='inventory_module.category')),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inventory_id', models.IntegerField()),
                ('inventory_name', models.CharField(max_length=20)),
                ('inventory_location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_id', models.CharField(max_length=10)),
                ('role_name', models.CharField(max_length=20)),
                ('role_func_modules', models.ManyToManyField(to='inventory_module.func_modules')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('user_passwd', models.CharField(max_length=20)),
                ('user_employee', models.ForeignKey(to='inventory_module.employee')),
                ('user_role', models.ForeignKey(to='inventory_module.role')),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vendor_id', models.CharField(max_length=10)),
                ('vendor_name', models.CharField(max_length=30)),
                ('vendor_country', models.CharField(max_length=20)),
                ('website_url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_inventory',
            field=models.ForeignKey(to='inventory_module.inventory'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_user',
            field=models.ForeignKey(related_name='user_goods_creator', to='inventory_module.user'),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_vendor',
            field=models.ForeignKey(to='inventory_module.vendor'),
        ),
        migrations.AddField(
            model_name='borrowe_goods_list',
            name='borrow_goods',
            field=models.ForeignKey(to='inventory_module.goods'),
        ),
        migrations.AddField(
            model_name='borrowe_goods_list',
            name='borrower',
            field=models.ForeignKey(related_name='borrower_in_user', to='inventory_module.user'),
        ),
    ]
