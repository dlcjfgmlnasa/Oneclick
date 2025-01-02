# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class Experiments(TimeStampedModel):
    SEX_STATE_CHOICE = ((0, 'MAN'), (1, 'WOMAN'))

    name = models.CharField(
        max_length=25,
        null=False, blank=False,
        db_column='SUBJECT_NAME'
    )
    age = models.IntegerField(
        null=True, blank=True,
        db_column='SUBJECT_AGE'
    )
    birth = models.DateField(
        null=True, blank=True,
        db_column='SUBJECT_BIRTH'
    )
    sex = models.CharField(
        max_length=10,
        null=True, blank=True,
        choices=SEX_STATE_CHOICE,
        db_column='SUBJECT_SEX'
    )
    measurement_date = models.DateTimeField(
        null=True, blank=True,
        db_column='MEASUREMENT_DATE'
    )
    hrv = models.ForeignKey(
        'ecg.HRV',
        related_name='experiments',
        null=True, on_delete=models.CASCADE,
        db_column='EXPERIMENT_HRV'
    )
    eeg = models.ForeignKey(
        'eeg.EEG',
        related_name='experiments',
        null=True, on_delete=models.CASCADE,
        db_column='EXPERIMENT_EEG'
    )
    questionnaire = models.ForeignKey(
        'survey.Questionnaire',
        related_name='experiments',
        null=True, on_delete=models.CASCADE,
        db_comment='EXPERIMENT_SURVEY'
    )

    class Meta:
        db_table = 'OC_EXPERIMENTS'
        ordering = ['-int_dt']

