# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_auto_20150302_1843'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rates',
            new_name='Rate',
        ),
    ]
