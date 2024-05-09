# -*- coding:utf-8 -*-
from ecg.models import *
from subjects.serializer import SubjectSerializer
from rest_framework import serializers


class BaseLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Baseline
        fields = (
            'pk',
            'mean_hr', 'mean_rr', 'sdnn', 'rmssd', 'pnn50', 'pnn20', 'pnn10', 'pnn05',
            'vlf', 'lf', 'hf', 'lf_hf_ratio',
            'sd1', 'sd2', 'sd1_sd2_ratio'
        )


class Stimulation1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stimulation1
        fields = (
            'pk',
            'mean_hr', 'mean_rr', 'sdnn', 'rmssd', 'pnn50', 'pnn20', 'pnn10', 'pnn05',
            'vlf', 'lf', 'hf', 'lf_hf_ratio',
            'sd1', 'sd2', 'sd1_sd2_ratio'
        )


class Recovery1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Recovery1
        fields = (
            'pk',
            'mean_hr', 'mean_rr', 'sdnn', 'rmssd', 'pnn50', 'pnn20', 'pnn10', 'pnn05',
            'vlf', 'lf', 'hf', 'lf_hf_ratio',
            'sd1', 'sd2', 'sd1_sd2_ratio'
        )


class Stimulation2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stimulation2
        fields = (
            'pk',
            'mean_hr', 'mean_rr', 'sdnn', 'rmssd', 'pnn50', 'pnn20', 'pnn10', 'pnn05',
            'vlf', 'lf', 'hf', 'lf_hf_ratio',
            'sd1', 'sd2', 'sd1_sd2_ratio'
        )


class Recovery2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Recovery2
        fields = (
            'pk',
            'mean_hr', 'mean_rr', 'sdnn', 'rmssd', 'pnn50', 'pnn20', 'pnn10', 'pnn05',
            'vlf', 'lf', 'hf', 'lf_hf_ratio',
            'sd1', 'sd2', 'sd1_sd2_ratio'
        )


class HRVSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    subject = SubjectSerializer(read_only=True)
    baseline = BaseLineSerializer(read_only=True)
    stimulation1 = Stimulation1Serializer(read_only=True)
    recovery1 = Recovery1Serializer(read_only=True)
    stimulation2 = Stimulation2Serializer(read_only=True)
    recovery2 = Recovery2Serializer(read_only=True)

    class Meta:
        model = HRV
        fields = (
            'pk',
            'subject',
            'measurement_date',
            'baseline',
            'stimulation1',
            'recovery1',
            'stimulation2',
            'recovery2',
        )
