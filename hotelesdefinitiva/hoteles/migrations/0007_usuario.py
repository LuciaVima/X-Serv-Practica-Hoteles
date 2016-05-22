# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0006_auto_20160517_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulopagina', models.CharField(max_length=150)),
                ('Nombre', models.CharField(max_length=32)),
                ('hotel_id', models.ForeignKey(to='hoteles.Hotel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
