# Generated by Django 4.2.7 on 2024-01-09 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='LastUpdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
