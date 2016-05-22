# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0016_auto_20160518_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulopagina', models.CharField(default=b'', max_length=150)),
                ('Nombre', models.CharField(max_length=32)),
                ('tama', models.CharField(max_length=32)),
                ('fondo', models.CharField(max_length=32)),
                ('hotel_id', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
