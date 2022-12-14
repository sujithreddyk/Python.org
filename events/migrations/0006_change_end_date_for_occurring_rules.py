# Generated by Django 1.11.5 on 2017-10-29 15:24

import datetime

from django.db import migrations
from django.db.models import F


def exclude_ending_day(apps, schema_editor):
    OccurringRule = apps.get_model('events', 'OccurringRule')
    db_alias = schema_editor.connection.alias
    OccurringRule.objects.using(db_alias)\
        .filter(all_day=True)\
        .update(dt_end=F('dt_end') - datetime.timedelta(days=1))


def include_ending_day(apps, schema_editor):
    OccurringRule = apps.get_model('events', 'OccurringRule')
    db_alias = schema_editor.connection.alias
    OccurringRule.objects.using(db_alias)\
        .filter(all_day=True)\
        .update(dt_end=F('dt_end') + datetime.timedelta(days=1))


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20170821_2000'),
    ]

    operations = [
        migrations.RunPython(exclude_ending_day, include_ending_day),
    ]
