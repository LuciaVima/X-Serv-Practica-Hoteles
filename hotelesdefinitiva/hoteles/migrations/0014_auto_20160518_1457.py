# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0013_auto_20160518_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='hotel_id',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='hotel_id',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='imagen',
            name='hotel_id',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='hotel_id',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
