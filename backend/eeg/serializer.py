# -*- coding:utf-8 -*-
from rest_framework import serializers
from eeg.models import EEG


class EEGSerializer(serializers.ModelSerializer):
    class Meta:
        model = EEG
