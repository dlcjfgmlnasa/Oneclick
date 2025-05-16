# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from survey.models import Questionnaire
from experiments.models import Experiments
from experiments.serializer import ExperimentsQuestionnaireSerializer
from survey.serializer import QuestionnaireSerializer


class QuestionnaireView(APIView):
    def post(self, requests, pk):
        try:
            model = Experiments.objects.get(pk=pk)
        except Experiments.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = QuestionnaireSerializer(data=requests.data)
        if serializer_cls.is_valid():
            serializer_cls.save()
            questionnaire = Questionnaire.objects.get(pk=serializer_cls.data['pk'])
            model.questionnaire = questionnaire
            model.save()

            return Response(
                data=serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class QuestionnaireListView(APIView):
    def get(self, requests):
        name = self.request.GET.get('name')
        birth = self.request.GET.get('birth')
        sex = self.request.GET.get('sex')

        try:
            exp = Experiments.objects.filter(
                name=name,
                birth=birth,
                sex=sex
            ).order_by('-measurement_date')
        except Experiments.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = ExperimentsQuestionnaireSerializer(exp, many=True)

        return Response(
            data=serializer_cls.data,
            status=status.HTTP_200_OK
        )
