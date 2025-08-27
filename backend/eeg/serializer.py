# -*- coding:utf-8 -*-
from rest_framework import serializers
from eeg.models import *


class EEGFrontalLimbicSerializer(serializers.ModelSerializer):
    class Meta:
        model = EEGFrontalLimbic
        fields = '__all__'

class EEGBaseLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = EEGBaseline
        fields = '__all__'


class EEGStimulation1Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGStimulation1
        fields = '__all__'


class EEGRecovery1Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGRecovery1
        fields = '__all__'


class EEGStimulation2Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGStimulation2
        fields = '__all__'


class EEGRecovery2Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGRecovery2
        fields = '__all__'


class EEGDiff1Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGDiff1
        fields = '__all__'


class EEGDiff2Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGDiff2
        fields = '__all__'


class EEGDiff3Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGDiff3
        fields = '__all__'


class EEGDiff4Serializer(serializers.ModelSerializer):
    class Meta:
        model = EEGDiff4
        fields = '__all__'

class EEGFaaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EEGFAA
        fields = '__all__'

class EEGSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(read_only=True)
    baseline = EEGBaseLineSerializer(read_only=True)
    frontal_limbic = EEGFrontalLimbicSerializer(read_only=True)
    stimulation1 = EEGStimulation1Serializer(read_only=True)
    recovery1 = EEGRecovery1Serializer(read_only=True)
    stimulation2 = EEGStimulation2Serializer(read_only=True)
    recovery2 = EEGRecovery2Serializer(read_only=True)
    diff1 = EEGDiff1Serializer(read_only=True)
    diff2 = EEGDiff2Serializer(read_only=True)
    diff3 = EEGDiff3Serializer(read_only=True)
    diff4 = EEGDiff4Serializer(read_only=True)
    faa = EEGFaaSerializer(read_only=True)

    class Meta:
        model = EEG
        fields = (
            'pk',
            'psd',
            'sleep_staging',
            'frontal_limbic',
            'baseline',
            'stimulation1',
            'recovery1',
            'stimulation2',
            'recovery2',
            'diff1',
            'diff2',
            'diff3',
            'diff4',
            'faa',
            'note',
        )


class EEGNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EEG
        fields = (
            'pk',
            'note'
        )
