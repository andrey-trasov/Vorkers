# Generated by Django 5.1.4 on 2024-12-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vorkers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=150, verbose_name="ФИО")),
                ("team_number", models.IntegerField(verbose_name="номер бригады")),
                ("salary", models.IntegerField(verbose_name="зарплата")),
                (
                    "specialization",
                    models.CharField(max_length=250, verbose_name="специализация"),
                ),
            ],
        ),
    ]
