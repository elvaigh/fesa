# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_profil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('price', models.FloatField()),
                ('published', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]