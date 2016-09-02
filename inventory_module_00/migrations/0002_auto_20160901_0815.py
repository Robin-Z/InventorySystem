# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowe_goods_list',
            name='return_date',
            field=models.DateField(null=True),
        ),
    ]
