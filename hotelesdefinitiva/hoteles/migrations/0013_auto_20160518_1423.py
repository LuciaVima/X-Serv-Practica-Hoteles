# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0012_auto_20160518_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='Fecha',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='Titulo',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Titulopagina',
            field=models.CharField(default=b'', max_length=150),
            preserve_default=True,
        ),
    ]
