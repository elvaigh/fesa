# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_offre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offre',
            old_name='name',
            new_name='titre',
        ),
    ]
