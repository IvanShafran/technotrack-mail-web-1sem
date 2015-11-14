# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='extuser',
            name='nickname',
            field=models.CharField(unique=True, max_length=40, verbose_name='\u041d\u0438\u043a\u043d\u0435\u0439\u043c', blank=True),
        ),
    ]
