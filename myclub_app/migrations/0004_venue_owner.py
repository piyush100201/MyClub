# Generated by Django 5.1.7 on 2025-03-26 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myclub_app', '0003_alter_event_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='owner',
            field=models.IntegerField(default=1, verbose_name='Venue Owner'),
        ),
    ]
