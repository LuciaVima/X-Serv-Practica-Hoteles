# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Titulo', models.CharField(max_length=32)),
                ('Cuerpo', models.TextField()),
                ('Fecha', models.DateField()),
                ('Autor', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('cuerpo', models.TextField()),
                ('url', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('pais', models.CharField(max_length=32)),
                ('latitud', models.IntegerField()),
                ('longitud', models.IntegerField()),
                ('subAA', models.CharField(max_length=32)),
                ('idTipo', models.IntegerField()),
                ('Tipo', models.CharField(max_length=32)),
                ('idCategoria', models.IntegerField()),
                ('Categoria', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=32)),
                ('hotel_id', models.ForeignKey(to='hoteles.Hotel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comentario',
            name='hotel_id',
            field=models.ForeignKey(to='hoteles.Hotel'),
            preserve_default=True,
        ),
    ]
