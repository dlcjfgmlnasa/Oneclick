# Generated by Django 4.2.11 on 2024-07-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eeg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eeg',
            name='note',
            field=models.TextField(blank=True, db_column='EEG_NOTE', null=True),
        ),
    ]