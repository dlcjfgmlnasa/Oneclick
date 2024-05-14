# -*- coding:utf-8 -*-
from django.db import models
from backend.model import TimeStampedModel


class EEG(TimeStampedModel):
    class Meta:
        db_table = 'OC_EEG'
