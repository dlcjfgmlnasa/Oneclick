# -*- coding:utf-8 -*-
from ecg.models import *
from rest_framework import serializers


class HRVBaseLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRVBaseline
        fields = '__all__'


class HRVStimulation1Serializer(serializers.ModelSerializer):
    class Meta:
        model = HRVStimulation1
        fields = '__all__'


class HRVRecovery1Serializer(serializers.ModelSerializer):
    class Meta:
        model = HRVRecovery1
        fields = '__all__'


class HRVStimulation2Serializer(serializers.ModelSerializer):
    class Meta:
        model = HRVStimulation2
        fields = '__all__'


class HRVRecovery2Serializer(serializers.ModelSerializer):
    class Meta:
        model = HRVRecovery2
        fields = '__all__'


class HRVSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    baseline = HRVBaseLineSerializer(read_only=True)
    stimulation1 = HRVStimulation1Serializer(read_only=True)
    recovery1 = HRVRecovery1Serializer(read_only=True)
    stimulation2 = HRVStimulation2Serializer(read_only=True)
    recovery2 = HRVRecovery2Serializer(read_only=True)

    class Meta:
        model = HRV
        fields = (
            'pk',
            'nni',
            'rmssd',
            'baseline',
            'stimulation1',
            'recovery1',
            'stimulation2',
            'recovery2',
        )
