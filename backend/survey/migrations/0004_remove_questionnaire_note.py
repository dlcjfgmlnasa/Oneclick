# Generated by Django 4.2.11 on 2025-01-02 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_questionnaire_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='note',
        ),
    ]