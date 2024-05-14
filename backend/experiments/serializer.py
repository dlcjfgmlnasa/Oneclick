# -*- coding:utf-8 -*-
from experiments.models import Experiments
from rest_framework import serializers
from ecg.serializer import HRVSerializer
from eeg.serializer import EEGSerializer


class ExperimentsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiments
        fields = '__all__'
