# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class HRV(TimeStampedModel):
    subject = models.ForeignKey(
        'subjects.Subject',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_SUBJECT_ID'
    )
    date = models.DateTimeField(
        null=False, blank=False,
        db_column='HRV_DATE'
    )
    baseline = models.ForeignKey(
        'ecg.Baseline',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_BASELINE_ID'
    )
    stimulation1 = models.ForeignKey(
        'ecg.Stimulation1',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_STIMULATION_1_ID'
    )
    recovery1 = models.ForeignKey(
        'ecg.Recovery1',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_RECOVERY_1_ID'
    )
    stimulation2 = models.ForeignKey(
        'ecg.Stimulation2',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_STIMULATION_2_ID'
    )
    recovery2 = models.ForeignKey(
        'ecg.Recovery2',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_RECOVERY_2_ID'
    )


class HRVParameter(TimeStampedModel):
    # 1. [Time-Domain Parameter]
    mean_hr = models.FloatField(
        null=True, blank=True,
        db_column='HRV_MEAN_HR'
    )
    mean_rr = models.FloatField(
        null=True, blank=True,
        db_column='HRV_MEAN_RR'
    )
    sdnn = models.FloatField(
        null=True, blank=True,
        db_column='HRV_SDNN'
    )
    rmssd = models.FloatField(
        null=True, blank=True,
        db_column='HRV_RMSSD'
    )
    pnn50 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_pNN50'
    )
    pnn20 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_pNN20'
    )
    pnn10 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_pNN10'
    )
    pnn05 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_pNN05'
    )
    # 2. [Frequency-Domain Parameter]
    vlf = models.FloatField(
        null=True, blank=True,
        db_column='HRV_VLF'
    )
    lf = models.FloatField(
        null=True, blank=True,
        db_column='HRV_LF'
    )
    hf = models.FloatField(
        null=True, blank=True,
        db_column='HRV_HF'
    )
    lf_hf_ratio = models.FloatField(
        null=True, blank=True,
        db_column='HRV_LF_HF_RATIO'
    )
    # 3. [Non-Linear Parameter]
    sd1 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_SD1'
    )
    sd2 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_SD2'
    )
    sd1_sd2_ratio = models.FloatField(
        null=True, blank=True,
        db_column='HRV_SD1_SD2_RATIO'
    )


class Baseline(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_BASELINE'


class Stimulation1(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_STIMULATION_1'


class Recovery1(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_RECOVERY_1'


class Stimulation2(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_STIMULATION_2'


class Recovery2(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_RECOVERY_2'
