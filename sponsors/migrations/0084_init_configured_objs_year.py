# Generated by Django 2.2.24 on 2022-07-29 16:28

from django.db import migrations

def populate_with_current_year(apps, schema_editor):
    SponsorshipPackage = apps.get_model("sponsors", "SponsorshipPackage")
    SponsorshipBenefit = apps.get_model("sponsors", "SponsorshipBenefit")
    SponsorshipCurrentYear = apps.get_model("sponsors", "SponsorshipCurrentYear")

    year = SponsorshipCurrentYear.objects.get().year

    SponsorshipPackage.objects.all().update(year=year)
    SponsorshipBenefit.objects.all().update(year=year)


def reset_current_year(apps, schema_editor):
    SponsorshipPackage = apps.get_model("sponsors", "SponsorshipPackage")
    SponsorshipBenefit = apps.get_model("sponsors", "SponsorshipBenefit")

    SponsorshipPackage.objects.all().update(year=None)
    SponsorshipBenefit.objects.all().update(year=None)



class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0083_auto_20220729_1624'),
    ]

    operations = [
        migrations.RunPython(populate_with_current_year, reset_current_year)
    ]
