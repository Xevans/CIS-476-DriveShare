# Generated by Django 5.0.3 on 2024-04-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_first_time",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="profile",
            name="sq1",
            field=models.CharField(default="", max_length=70),
        ),
        migrations.AddField(
            model_name="profile",
            name="sq2",
            field=models.CharField(default="", max_length=70),
        ),
    ]
