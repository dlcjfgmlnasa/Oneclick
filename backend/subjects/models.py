# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class Subject(TimeStampedModel):
    SEX_STATE_CHOICE = (
        (1, 'man'),
        (2, 'woman'),
    )
    name = models.CharField(
        max_length=25,
        null=False, blank=False,
        db_column='SUBJECT_NAME'
    )
    age = models.IntegerField(
        null=False, blank=False,
        db_column='SUBJECT_AGE'
    )
    birth = models.DateField(
        null=False, blank=False,
        db_column='SUBJECT_BIRTH'
    )
    sex = models.CharField(
        max_length=10,
        null=False, blank=False,
        choices=SEX_STATE_CHOICE,
        db_column='SUBJECT_SEX'
    )

    class Meta:
        db_table = 'OC_USER'
        ordering = ['id']
        unique_together = ['name', 'age', 'birth']
