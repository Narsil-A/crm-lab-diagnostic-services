# Generated by Django 4.2.5 on 2023-10-12 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosticService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BRU', 'Brucellosis'), ('MYC', 'Mycobacteria Bovina'), ('LEP', 'Leptospirosis'), ('RAB', 'Rabia'), ('FIE', 'Fiebre Aftosa')], max_length=3)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField(help_text='Duration in minutes')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_diagnostic_services', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
