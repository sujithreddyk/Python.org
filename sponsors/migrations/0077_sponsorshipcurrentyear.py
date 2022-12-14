# Generated by Django 2.2.24 on 2022-07-28 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0076_auto_20220728_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorshipCurrentYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(limit_value=2022, message='The min year value is 2022.'), django.core.validators.MaxValueValidator(limit_value=2050, message='The max year value is 2050.')])),
            ],
        ),
    ]
