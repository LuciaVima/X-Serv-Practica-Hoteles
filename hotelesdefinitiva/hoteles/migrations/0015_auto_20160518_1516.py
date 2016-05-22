# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0014_auto_20160518_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='idTipo',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
