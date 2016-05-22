# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0004_auto_20160517_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='subCategoria',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]
