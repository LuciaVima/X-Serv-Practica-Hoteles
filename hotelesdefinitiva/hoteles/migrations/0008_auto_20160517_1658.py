# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0007_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='url',
            new_name='web',
        ),
    ]
