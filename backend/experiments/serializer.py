# -*- coding:utf-8 -*-
from experiments.models import Experiments
from rest_framework import serializers
from survey.serializer import QuestionnaireSerializer


class ExperimentsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiments
        fields = '__all__'


class ExperimentsQuestionnaireSerializer(serializers.ModelSerializer):
    questionnaire = QuestionnaireSerializer()

    class Meta:
        model = Experiments
        fields = (
            'pk',
            'measurement_date',
            'questionnaire'
        )
