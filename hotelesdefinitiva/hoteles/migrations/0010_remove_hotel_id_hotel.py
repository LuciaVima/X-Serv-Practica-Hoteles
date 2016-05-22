# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0009_auto_20160518_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='id_hotel',
        ),
    ]
