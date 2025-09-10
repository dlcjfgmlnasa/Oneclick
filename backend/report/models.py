# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class Report(models.Model):
    
    tib = models.FloatField(
        null = True, blank = True,
        db_column='TIB'
    )

    tst = models.FloatField(
        null = True, blank = True,
        db_column='TST'
    )

    twt = models.FloatField(
        null = True, blank = True,
        db_column='TWT'
    )

    waso = models.FloatField(
        null = True, blank = True,
        db_column='WASO'
    )

    sleep_latency = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_LATENCY'
    )

    rem_latency = models.FloatField(
        null = True, blank = True,
        db_column='REM_LATENCY'
    )

    sleep_eff = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_EFF'
    )

    sleep_n1_min = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_N1_MIN'
    )

    sleep_n2_min = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_N2_MIN'
    )

    sleep_n3_min = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_N3_MIN'
    )

    sleep_nrem_min = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_NREM_MIN'
    )

    sleep_rem_min = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_REM_MIN'
    )

    sleep_n1_tst = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_N1_TST'
    )

    sleep_n2_tst = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_N2_TST'
    )

    sleep_n3_tst = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_N3_TST'
    )

    sleep_nrem_tst = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_NREM_TST'
    )

    sleep_rem_tst = models.FloatField(
        null = True, blank = True,
        db_column='SLEEP_REM_TST'
    )

    class Meta:
        db_table = 'OC_REPORT'