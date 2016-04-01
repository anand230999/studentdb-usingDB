# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studid', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField(default=0)),
                ('marks', models.IntegerField(default=0)),
                ('sex', models.CharField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
