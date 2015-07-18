# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150714_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='champion',
            old_name='champion_champion_id',
            new_name='champion_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_item_id',
            new_name='item_id',
        ),
    ]
