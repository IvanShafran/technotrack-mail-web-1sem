# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extuser', '0006_auto_20151114_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extuser',
            name='nickname',
        ),
    ]
