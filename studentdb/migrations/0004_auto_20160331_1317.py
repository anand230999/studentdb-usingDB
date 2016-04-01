# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdb', '0003_auto_20160331_1310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='studid',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
