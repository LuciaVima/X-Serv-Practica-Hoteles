# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0002_auto_20160517_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='Autor',
        ),
        migrations.AddField(
            model_name='hotel',
            name='NumComentarios',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
