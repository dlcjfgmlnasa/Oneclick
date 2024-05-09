# -*- coding:utf-8 -*-
from subjects.models import Subject
from rest_framework import serializers


class SubjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'pk',
            'name',
            'age',
            'birth',
            'sex',
        )


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'pk',
            'name',
            'age',
            'birth',
            'sex',
            'int_dt',
            'upt_dt'
        )
