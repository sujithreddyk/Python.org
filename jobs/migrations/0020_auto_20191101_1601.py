# Generated by Django 2.0.13 on 2019-11-01 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_job_submitted_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.URLField(null=True, verbose_name='URL'),
        ),
    ]