# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0018_elegidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='elegidos',
            name='Fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 19, 20, 35, 33, 889075)),
            preserve_default=True,
        ),
    ]
