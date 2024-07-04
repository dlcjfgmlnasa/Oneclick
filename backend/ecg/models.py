# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class HRV(TimeStampedModel):
    nni = models.JSONField(
        null=True,
        db_column='HRV_NNI'
    )
    rmssd = models.JSONField(
        null=True,
        db_column='HRV_RMSSD'
    )
    baseline = models.ForeignKey(
        'ecg.HRVBaseline',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_BASELINE_ID'
    )
    stimulation1 = models.ForeignKey(
        'ecg.HRVStimulation1',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_STIMULATION_1_ID'
    )
    recovery1 = models.ForeignKey(
        'ecg.HRVRecovery1',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_RECOVERY_1_ID'
    )
    stimulation2 = models.ForeignKey(
        'ecg.HRVStimulation2',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_STIMULATION_2_ID'
    )
    recovery2 = models.ForeignKey(
        'ecg.HRVRecovery2',
        null=True, on_delete=models.CASCADE,
        related_name='hrv', db_column='HRV_RECOVERY_2_ID'
    )

    class Meta:
        db_table = 'OC_HRV'


class HRVParameter(TimeStampedModel):
    # >> 1. Time-Domain
    sdnn = models.FloatField(
        null=True, blank=True,
        db_column='HRV_SDNN'
    )
    rmssd = models.FloatField(
        null=True, blank=True,
        db_column='HRV_RMSSD'
    )
    sdsd = models.FloatField(
        null=True, blank=True,
        db_column='HRV_SDSD'
    )
    nn50 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_NN50'
    )
    pnn50 = models.FloatField(
        null=True, blank=True,
        db_column='HRV_pNN50'
    )
    tri_index = models.FloatField(
        null=True, blank=True,
        db_column='HRV_TRI_Index'
    )

    # >> 2. Frequency-Domain
    vlf_rel_power = models.FloatField(
        null=True, blank=True,
        db_column='HRV_REL_VLF'
    )
    lf_rel_power = models.FloatField(
        null=True, blank=True,
        db_column='HRV_REL_LF'
    )
    hf_rel_power = models.FloatField(
        null=True, blank=True,
        db_column='HRV_REF_HF'
    )
    lh_ratio = models.FloatField(
        null=True, blank=True,
        db_column='HRV_LH_RATIO'
    )
    norm_lf = models.FloatField(
        null=True, blank=True,
        db_column='HRV_NORM_LF'
    )
    norm_hf = models.FloatField(
        null=True, blank=True,
        db_column='HRV_NORM_HF'
    )
    psd = models.JSONField(
        null=False,
        db_column='HRV_PSD'
    )
    heart_rate = models.ImageField(
        null=False, blank=False,
        db_column='HRV_HEAD_RATE'
    )
    comparison = models.ImageField(
        null=False, blank=False,
        db_column='HRV_COMPARISON'
    )

    class Meta:
        abstract = True


class HRVBaseline(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_BASELINE'


class HRVStimulation1(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_STIMULATION_1'


class HRVRecovery1(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_RECOVERY_1'


class HRVStimulation2(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_STIMULATION_2'


class HRVRecovery2(HRVParameter):
    class Meta:
        db_table = 'OC_HRV_RECOVERY_2'
