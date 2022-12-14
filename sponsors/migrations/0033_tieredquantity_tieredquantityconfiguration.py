# Generated by Django 2.0.13 on 2021-07-26 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sponsors", "0032_sponsorcontact_accounting"),
    ]

    operations = [
        migrations.CreateModel(
            name="TieredQuantity",
            fields=[
                (
                    "benefitfeature_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="sponsors.BenefitFeature",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sponsors.SponsorshipPackage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tiered Quantity",
                "verbose_name_plural": "Tiered Quantities",
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("sponsors.benefitfeature", models.Model),
        ),
        migrations.CreateModel(
            name="TieredQuantityConfiguration",
            fields=[
                (
                    "benefitfeatureconfiguration_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="sponsors.BenefitFeatureConfiguration",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                (
                    "package",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sponsors.SponsorshipPackage",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tiered Benefit Configuration",
                "verbose_name_plural": "Tiered Benefit Configurations",
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("sponsors.benefitfeatureconfiguration", models.Model),
        ),
    ]
