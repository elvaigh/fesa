# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_offre_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offre',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
