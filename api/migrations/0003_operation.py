# Generated by Django 4.1.2 on 2022-11-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_profile_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="Operation",
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
                ("slackUsername", models.CharField(default="maestro", max_length=20)),
                ("result", models.IntegerField(blank=True, null=True)),
                ("operation_type", models.CharField(max_length=255)),
                ("x", models.IntegerField()),
                ("y", models.IntegerField()),
            ],
        ),
    ]
