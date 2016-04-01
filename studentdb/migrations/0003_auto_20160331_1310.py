# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdb', '0002_auto_20160331_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(default=b'NotSpecified', max_length=13),
        ),
        migrations.AlterField(
            model_name='student',
            name='studid',
            field=models.IntegerField(unique=True),
        ),
    ]
