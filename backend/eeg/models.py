# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class EEG(TimeStampedModel):
    psd = models.JSONField(
        null=False,
        db_column='EEG_PSD'
    )
    sleep_staging = models.JSONField(
        null=False,
        db_column='EEG_SLEEP_STAGING'
    )
    frontal_limbic = models.ForeignKey(
        'eeg.EEGFrontalLimbic',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_FRONTAL_LIMBIC_ID'
    )
    baseline = models.ForeignKey(
        'eeg.EEGBaseline',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_BASELINE_ID'
    )
    stimulation1 = models.ForeignKey(
        'eeg.EEGStimulation1',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_STIMULATION_1_ID'
    )
    recovery1 = models.ForeignKey(
        'eeg.EEGRecovery1',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_RECOVERY_1_ID'
    )
    stimulation2 = models.ForeignKey(
        'eeg.EEGStimulation2',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_STIMULATION_2_ID'
    )
    recovery2 = models.ForeignKey(
        'eeg.EEGRecovery2',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_RECOVERY_2_ID'
    )
    diff1 = models.ForeignKey(
        'eeg.EEGDiff1',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_DIFF_1_ID'
    )
    diff2 = models.ForeignKey(
        'eeg.EEGDiff2',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_DIFF_2_ID'
    )
    diff3 = models.ForeignKey(
        'eeg.EEGDiff3',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_DIFF_3_ID'
    )
    diff4 = models.ForeignKey(
        'eeg.EEGDiff4',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_DIFF_4_ID'
    )
    faa = models.ForeignKey(
        'eeg.EEGFAA',
        null=True, on_delete=models.CASCADE,
        related_name='eeg', db_column='EEG_FAA_ID'
    )
    

    note = models.TextField(
        null=True, blank=True,
        db_column='EEG_NOTE'
    )

    class Meta:
        db_table = 'OC_EEG'


class EEGFrontalLimbic(TimeStampedModel):
    delta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_LIMBIC_DELTA'
    )
    theta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_LIMBIC_THETA'
    )
    alpha = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_LIMBIC_ALPHA'
    )
    beta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_LIMBIC_BETA'
    )
    gamma = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_LIMBIC_GAMMA'
    )

class EEGFAA(TimeStampedModel):
    delta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_ASYMMETRY_DELTA'
    )
    theta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_ASYMMETRY_THETA'
    )
    alpha = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_ASYMMETRY_ALPHA'
    )
    beta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_ASYMMETRY_BETA'
    )
    gamma = models.ImageField(
        null=False, blank=False,
        db_column='EEG_FRONTAL_ASYMMETRY_GAMMA'
    )

    class Meta:
        db_table = 'OC_EEG_FAA'


class EEGParameter(TimeStampedModel):
    topography_delta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_TOPOGRAPHY_DELTA'
    )
    topography_theta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_TOPOGRAPHY_THETA'
    )
    topography_alpha = models.ImageField(
        null=False, blank=False,
        db_column='EEG_TOPOGRAPHY_ALPHA'
    )
    topography_beta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_TOPOGRAPHY_BETA'
    )
    topography_gamma = models.ImageField(
        null=False, blank=False,
        db_column='EEG_TOPOGRAPHY_GAMMA'
    )

    connectivity_delta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_CONNECTIVITY_DELTA_COH'
    )
    connectivity_theta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_CONNECTIVITY_THETA_COH'
    )
    connectivity_alpha = models.ImageField(
        null=False, blank=False,
        db_column='EEG_CONNECTIVITY_ALPHA_COH'
    )
    connectivity_beta = models.ImageField(
        null=False, blank=False,
        db_column='EEG_CONNECTIVITY_BETA_COH'
    )
    connectivity_gamma = models.ImageField(
        null=False, blank=False,
        db_column='EEG_CONNECTIVITY_GAMMA_COH'
    )

    connectivity2_delta = models.ImageField(
        null=True, blank=True,
        db_column='EEG_CONNECTIVITY_DELTA_PLV'
    )
    connectivity2_theta = models.ImageField(
        null=True, blank=True,
        db_column='EEG_CONNECTIVITY_THETA_PLV'
    )
    connectivity2_alpha = models.ImageField(
        null=True, blank=True,
        db_column='EEG_CONNECTIVITY_ALPHA_PLV'
    )
    connectivity2_beta = models.ImageField(
        null=True, blank=True,
        db_column='EEG_CONNECTIVITY_BETA_PLV'
    )
    connectivity2_gamma = models.ImageField(
        null=True, blank=True,
        db_column='EEG_CONNECTIVITY_GAMMA_PLV'
    )
    faa = models.ImageField(
        null=True, blank=True,
        db_column='EEG_FRONTAL_ALPHA_ASYMMETRY'
    )

    class Meta:
        abstract = True


class EEGBaseline(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_BASELINE'


class EEGStimulation1(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_STIMULATION_1'


class EEGRecovery1(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_RECOVERY_1'


class EEGStimulation2(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_STIMULATION_2'


class EEGRecovery2(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_RECOVERY_2'


class EEGDiff1(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_DIFF_1'


class EEGDiff2(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_DIFF_2'


class EEGDiff3(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_DIFF_3'


class EEGDiff4(EEGParameter):
    class Meta:
        db_table = 'OC_EEG_DIFF_4'
