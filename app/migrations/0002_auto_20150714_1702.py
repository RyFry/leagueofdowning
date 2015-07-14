# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='champion',
            old_name='champion_id',
            new_name='champion_champion_id',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_id',
            new_name='item_item_id',
        ),
    ]
