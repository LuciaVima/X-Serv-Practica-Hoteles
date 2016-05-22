# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0015_auto_20160518_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='idSubCategoria',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='idTipo',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
