# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0010_remove_hotel_id_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='hotel_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
