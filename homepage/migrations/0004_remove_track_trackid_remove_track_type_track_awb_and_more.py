# Generated by Django 4.2.7 on 2024-01-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_track_lastupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='TrackID',
        ),
        migrations.RemoveField(
            model_name='track',
            name='Type',
        ),
        migrations.AddField(
            model_name='track',
            name='AWB',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='track',
            name='CIGM',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='track',
            name='FC',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='track',
            name='GIGM',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='track',
            name='HBL',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='track',
            name='MBL',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='track',
            name='RO',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='track',
            name='Details',
            field=models.CharField(default='', max_length=1000),
        ),
    ]