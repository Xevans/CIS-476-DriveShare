# Generated by Django 5.0.3 on 2024-04-07 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_is_first_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="sq3",
            field=models.CharField(default="", max_length=70),
        ),
    ]
