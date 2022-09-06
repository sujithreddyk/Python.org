# Generated by Django 2.2.24 on 2022-08-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0091_sponsorshippackage_allow_a_la_carte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorshipbenefit',
            name='unavailable',
            field=models.BooleanField(default=False, help_text='If selected, this benefit will not be visible or available to applicants.', verbose_name='Benefit is unavailable'),
        ),
    ]