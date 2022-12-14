# Generated by Django 2.2.24 on 2022-01-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0067_sponsorbenefit_a_la_carte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='for_modified_package',
            field=models.BooleanField(default=False, help_text="If true, it means the user customized the package's benefits. Changes are listed under section 'User Customizations'."),
        ),
    ]
