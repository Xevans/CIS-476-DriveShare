# Generated by Django 5.0.3 on 2024-04-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0007_rentaltansactionhistory"),
    ]

    operations = [
        migrations.AddField(
            model_name="rentalapplication",
            name="message",
            field=models.TextField(default=""),
        ),
    ]
