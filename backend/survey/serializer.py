# -*- coding:utf-8 -*-
from survey.models import Questionnaire
from rest_framework import serializers


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            'pk',
            'irls',
            'psql',
            'isi',
            'ess',
            'compass31',
            'bai',
            'bdi2',
        )

