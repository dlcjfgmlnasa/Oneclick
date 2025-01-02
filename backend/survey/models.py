# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class Questionnaire(TimeStampedModel):
    irls = models.IntegerField(
        null=True, blank=True,
        db_column='IRLS'
    )
    psql = models.IntegerField(
        null=True, blank=True,
        db_column='PSQL'
    )
    isi = models.IntegerField(
        null=True, blank=True,
        db_column='ISI'
    )
    ess = models.IntegerField(
        null=True, blank=True,
        db_column='ESS'
    )
    compass31 = models.FloatField(
        null=True, blank=True,
        db_column='COMPASS31'
    )
    bai = models.IntegerField(
        null=True, blank=True,
        db_column='BAI'
    )
    bdi2 = models.IntegerField(
        null=True, blank=True,
        db_column='BDI2'
    )

    class Meta:
        db_table = 'OC_QUESTIONNAIRE'
