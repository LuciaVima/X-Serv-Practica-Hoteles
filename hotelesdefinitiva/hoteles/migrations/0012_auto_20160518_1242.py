# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0011_hotel_hotel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='hotel_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
