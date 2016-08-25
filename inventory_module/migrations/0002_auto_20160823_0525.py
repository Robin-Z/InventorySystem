# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='goods',
            name='goods_unit',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
