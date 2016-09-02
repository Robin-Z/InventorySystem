# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0002_auto_20160901_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowe_goods_list',
            name='return_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
