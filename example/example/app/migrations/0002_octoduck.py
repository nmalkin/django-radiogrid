# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import radiogrid.db


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Octoduck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('week', radiogrid.db.RadioGridField(require_all_fields=True, rows=((1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')), values=((1, '2-3 hours'), (2, '3-4 hours'), ('3', '5-7 hours'), (4, '8 hours'), (5, 'Never')))),
            ],
        ),
    ]
