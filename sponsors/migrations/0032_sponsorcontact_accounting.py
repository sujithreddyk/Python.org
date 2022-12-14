# Generated by Django 2.0.13 on 2021-08-10 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0031_auto_20210810_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorcontact',
            name='accounting',
            field=models.BooleanField(default=False, help_text='Accounting contacts will only be notified regarding invoices and payments.'),
        ),
    ]
