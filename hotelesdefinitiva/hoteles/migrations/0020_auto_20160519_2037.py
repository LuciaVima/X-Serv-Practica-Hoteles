# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0019_elegidos_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elegidos',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 19, 20, 37, 35, 779694)),
            preserve_default=True,
        ),
    ]
