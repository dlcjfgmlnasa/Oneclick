# -*- coding:utf-8 -*-
from ecg.models import *
from rest_framework import serializers


class BaseLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baseline
        fields = '__all__'


class Stimulation1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stimulation1
        fields = '__all__'


class Recovery1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Recovery1
        fields = '__all__'


class Stimulation2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stimulation2
        fields = '__all__'


class Recovery2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Recovery2
        fields = '__all__'


class HRVSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    baseline = BaseLineSerializer(read_only=True)
    stimulation1 = Stimulation1Serializer(read_only=True)
    recovery1 = Recovery1Serializer(read_only=True)
    stimulation2 = Stimulation2Serializer(read_only=True)
    recovery2 = Recovery2Serializer(read_only=True)

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
