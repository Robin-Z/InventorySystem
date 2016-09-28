# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_goods_list',
            name='borrow_goods',
            field=models.ForeignKey(related_name='borrow_good_in_goods', to='inventory_module.goods'),
        ),
        migrations.AlterField(
            model_name='borrow_goods_list',
            name='borrower',
            field=models.ForeignKey(related_name='borrower_in_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
