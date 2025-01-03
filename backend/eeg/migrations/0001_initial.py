# Generated by Django 4.2.11 on 2024-07-16 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EEGBaseline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('topography_delta', models.ImageField(db_column='EEG_TOPOGRAPHY_DELTA', upload_to='')),
                ('topography_theta', models.ImageField(db_column='EEG_TOPOGRAPHY_THETA', upload_to='')),
                ('topography_alpha', models.ImageField(db_column='EEG_TOPOGRAPHY_ALPHA', upload_to='')),
                ('topography_beta', models.ImageField(db_column='EEG_TOPOGRAPHY_BETA', upload_to='')),
                ('topography_gamma', models.ImageField(db_column='EEG_TOPOGRAPHY_GAMMA', upload_to='')),
                ('connectivity_delta', models.ImageField(db_column='EEG_CONNECTIVITY_DELTA', upload_to='')),
                ('connectivity_theta', models.ImageField(db_column='EEG_CONNECTIVITY_THETA', upload_to='')),
                ('connectivity_alpha', models.ImageField(db_column='EEG_CONNECTIVITY_ALPHA', upload_to='')),
                ('connectivity_beta', models.ImageField(db_column='EEG_CONNECTIVITY_BETA', upload_to='')),
                ('connectivity_gamma', models.ImageField(db_column='EEG_CONNECTIVITY_GAMMA', upload_to='')),
            ],
            options={
                'db_table': 'OC_EEG_BASELINE',
            },
        ),
        migrations.CreateModel(
            name='EEGFrontalLimBic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('delta', models.ImageField(db_column='EEG_FRONTAL_LIMBIC_DELTA', upload_to='')),
                ('theta', models.ImageField(db_column='EEG_FRONTAL_LIMBIC_THETA', upload_to='')),
                ('alpha', models.ImageField(db_column='EEG_FRONTAL_LIMBIC_ALPHA', upload_to='')),
                ('beta', models.ImageField(db_column='EEG_FRONTAL_LIMBIC_BETA', upload_to='')),
                ('gamma', models.ImageField(db_column='EEG_FRONTAL_LIMBIC_GAMMA', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EEGRecovery1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('topography_delta', models.ImageField(db_column='EEG_TOPOGRAPHY_DELTA', upload_to='')),
                ('topography_theta', models.ImageField(db_column='EEG_TOPOGRAPHY_THETA', upload_to='')),
                ('topography_alpha', models.ImageField(db_column='EEG_TOPOGRAPHY_ALPHA', upload_to='')),
                ('topography_beta', models.ImageField(db_column='EEG_TOPOGRAPHY_BETA', upload_to='')),
                ('topography_gamma', models.ImageField(db_column='EEG_TOPOGRAPHY_GAMMA', upload_to='')),
                ('connectivity_delta', models.ImageField(db_column='EEG_CONNECTIVITY_DELTA', upload_to='')),
                ('connectivity_theta', models.ImageField(db_column='EEG_CONNECTIVITY_THETA', upload_to='')),
                ('connectivity_alpha', models.ImageField(db_column='EEG_CONNECTIVITY_ALPHA', upload_to='')),
                ('connectivity_beta', models.ImageField(db_column='EEG_CONNECTIVITY_BETA', upload_to='')),
                ('connectivity_gamma', models.ImageField(db_column='EEG_CONNECTIVITY_GAMMA', upload_to='')),
            ],
            options={
                'db_table': 'OC_EEG_RECOVERY_1',
            },
        ),
        migrations.CreateModel(
            name='EEGRecovery2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('topography_delta', models.ImageField(db_column='EEG_TOPOGRAPHY_DELTA', upload_to='')),
                ('topography_theta', models.ImageField(db_column='EEG_TOPOGRAPHY_THETA', upload_to='')),
                ('topography_alpha', models.ImageField(db_column='EEG_TOPOGRAPHY_ALPHA', upload_to='')),
                ('topography_beta', models.ImageField(db_column='EEG_TOPOGRAPHY_BETA', upload_to='')),
                ('topography_gamma', models.ImageField(db_column='EEG_TOPOGRAPHY_GAMMA', upload_to='')),
                ('connectivity_delta', models.ImageField(db_column='EEG_CONNECTIVITY_DELTA', upload_to='')),
                ('connectivity_theta', models.ImageField(db_column='EEG_CONNECTIVITY_THETA', upload_to='')),
                ('connectivity_alpha', models.ImageField(db_column='EEG_CONNECTIVITY_ALPHA', upload_to='')),
                ('connectivity_beta', models.ImageField(db_column='EEG_CONNECTIVITY_BETA', upload_to='')),
                ('connectivity_gamma', models.ImageField(db_column='EEG_CONNECTIVITY_GAMMA', upload_to='')),
            ],
            options={
                'db_table': 'OC_EEG_RECOVERY_2',
            },
        ),
        migrations.CreateModel(
            name='EEGStimulation1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('topography_delta', models.ImageField(db_column='EEG_TOPOGRAPHY_DELTA', upload_to='')),
                ('topography_theta', models.ImageField(db_column='EEG_TOPOGRAPHY_THETA', upload_to='')),
                ('topography_alpha', models.ImageField(db_column='EEG_TOPOGRAPHY_ALPHA', upload_to='')),
                ('topography_beta', models.ImageField(db_column='EEG_TOPOGRAPHY_BETA', upload_to='')),
                ('topography_gamma', models.ImageField(db_column='EEG_TOPOGRAPHY_GAMMA', upload_to='')),
                ('connectivity_delta', models.ImageField(db_column='EEG_CONNECTIVITY_DELTA', upload_to='')),
                ('connectivity_theta', models.ImageField(db_column='EEG_CONNECTIVITY_THETA', upload_to='')),
                ('connectivity_alpha', models.ImageField(db_column='EEG_CONNECTIVITY_ALPHA', upload_to='')),
                ('connectivity_beta', models.ImageField(db_column='EEG_CONNECTIVITY_BETA', upload_to='')),
                ('connectivity_gamma', models.ImageField(db_column='EEG_CONNECTIVITY_GAMMA', upload_to='')),
            ],
            options={
                'db_table': 'OC_EEG_STIMULATION_1',
            },
        ),
        migrations.CreateModel(
            name='EEGStimulation2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('topography_delta', models.ImageField(db_column='EEG_TOPOGRAPHY_DELTA', upload_to='')),
                ('topography_theta', models.ImageField(db_column='EEG_TOPOGRAPHY_THETA', upload_to='')),
                ('topography_alpha', models.ImageField(db_column='EEG_TOPOGRAPHY_ALPHA', upload_to='')),
                ('topography_beta', models.ImageField(db_column='EEG_TOPOGRAPHY_BETA', upload_to='')),
                ('topography_gamma', models.ImageField(db_column='EEG_TOPOGRAPHY_GAMMA', upload_to='')),
                ('connectivity_delta', models.ImageField(db_column='EEG_CONNECTIVITY_DELTA', upload_to='')),
                ('connectivity_theta', models.ImageField(db_column='EEG_CONNECTIVITY_THETA', upload_to='')),
                ('connectivity_alpha', models.ImageField(db_column='EEG_CONNECTIVITY_ALPHA', upload_to='')),
                ('connectivity_beta', models.ImageField(db_column='EEG_CONNECTIVITY_BETA', upload_to='')),
                ('connectivity_gamma', models.ImageField(db_column='EEG_CONNECTIVITY_GAMMA', upload_to='')),
            ],
            options={
                'db_table': 'OC_EEG_STIMULATION_2',
            },
        ),
        migrations.CreateModel(
            name='EEG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('psd', models.JSONField(db_column='EEG_PSD')),
                ('sleep_staging', models.JSONField(db_column='EEG_SLEEP_STAGING')),
                ('baseline', models.ForeignKey(db_column='EEG_BASELINE_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eeg', to='eeg.eegbaseline')),
                ('frontal_limbic', models.ForeignKey(db_column='EEG_FRONTAL_LIMBIC_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eeg', to='eeg.eegfrontallimbic')),
                ('recovery1', models.ForeignKey(db_column='EEG_RECOVERY_1_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eeg', to='eeg.eegrecovery1')),
                ('recovery2', models.ForeignKey(db_column='EEG_RECOVERY_2_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eeg', to='eeg.eegrecovery2')),
                ('stimulation1', models.ForeignKey(db_column='EEG_STIMULATION_1_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eeg', to='eeg.eegstimulation1')),
                ('stimulation2', models.ForeignKey(db_column='EEG_STIMULATION_2_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eeg', to='eeg.eegstimulation2')),
            ],
            options={
                'db_table': 'OC_EEG',
            },
        ),
    ]
