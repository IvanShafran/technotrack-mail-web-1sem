# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0003_auto_20151114_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extuser',
            name='nickname',
            field=models.CharField(max_length=40, null=True, verbose_name='\u041d\u0438\u043a\u043d\u0435\u0439\u043c', blank=True),
        ),
    ]
