# Generated by Django 2.2.24 on 2022-07-30 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0084_init_configured_objs_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='year',
            field=models.PositiveIntegerField(db_index=True, null=True, validators=[django.core.validators.MinValueValidator(limit_value=2022, message='The min year value is 2022.'), django.core.validators.MaxValueValidator(limit_value=2050, message='The max year value is 2050.')]),
        ),
        migrations.AlterField(
            model_name='sponsorshipbenefit',
            name='year',
            field=models.PositiveIntegerField(db_index=True, null=True, validators=[django.core.validators.MinValueValidator(limit_value=2022, message='The min year value is 2022.'), django.core.validators.MaxValueValidator(limit_value=2050, message='The max year value is 2050.')]),
        ),
        migrations.AlterField(
            model_name='sponsorshippackage',
            name='year',
            field=models.PositiveIntegerField(db_index=True, null=True, validators=[django.core.validators.MinValueValidator(limit_value=2022, message='The min year value is 2022.'), django.core.validators.MaxValueValidator(limit_value=2050, message='The max year value is 2050.')]),
        ),
    ]
