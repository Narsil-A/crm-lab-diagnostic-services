# Generated by Django 4.2.5 on 2023-11-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="role",
            field=models.CharField(
                choices=[("lab_staff", "Lab Staff"), ("client", "Client")],
                default="client",
                max_length=10,
            ),
        ),
    ]