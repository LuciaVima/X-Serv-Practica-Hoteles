# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0005_auto_20160517_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='url',
            field=models.CharField(max_length=60),
            preserve_default=True,
        ),
    ]
