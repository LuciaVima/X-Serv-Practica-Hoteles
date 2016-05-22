# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0003_auto_20160517_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='idSubCategoria',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hotel',
            name='subCategoria',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='telefono',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='url',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
