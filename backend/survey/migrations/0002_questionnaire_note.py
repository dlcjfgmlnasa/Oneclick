# Generated by Django 4.2.11 on 2025-01-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='note',
            field=models.TextField(blank=True, db_column='QUESTIONNAIRE_NOTE', null=True),
        ),
    ]