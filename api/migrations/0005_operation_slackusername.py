# Generated by Django 4.1.2 on 2022-11-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_operation_slackusername"),
    ]

    operations = [
        migrations.AddField(
            model_name="operation",
            name="slackUsername",
            field=models.CharField(default="maestro", max_length=20),
        ),
    ]
