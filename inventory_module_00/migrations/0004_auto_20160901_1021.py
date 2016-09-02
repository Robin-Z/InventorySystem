# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0003_auto_20160901_0826'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrow_goods_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borrow_goods_qty', models.IntegerField()),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField(null=True, blank=True)),
                ('borrow_status', models.CharField(default=b'Open', max_length=10)),
                ('borrow_goods', models.ForeignKey(to='inventory_module.goods')),
                ('borrower', models.ForeignKey(related_name='borrower_in_user', to='inventory_module.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='borrowe_goods_list',
            name='borrow_goods',
        ),
        migrations.RemoveField(
            model_name='borrowe_goods_list',
            name='borrower',
        ),
        migrations.DeleteModel(
            name='borrowe_goods_list',
        ),
    ]
