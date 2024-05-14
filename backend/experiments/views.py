# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .serializer import ExperimentsViewSerializer
from .models import Experiments
from ecg.models import *
from eeg.models import *
from django.db.models import Q


class ExperimentsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ExperimentView(APIView):
    @staticmethod
    def get_value(data, param_name):
        try:
            value = data[param_name]
        except KeyError:
            value = None
        return value

    def post(self, request):
        data = request.data
        try:
            hrv = HRV.objects.create(
                nni=eval(data['hrv'])['nni'],
                rmssd=eval(data['hrv'])['rmssd'],
                baseline=Baseline.objects.create(**eval(data['hrv'])['baseline']),
                stimulation1=Stimulation1.objects.create(**eval(data['hrv'])['stimulation1']),
                recovery1=Recovery1.objects.create(**eval(data['hrv'])['recovery1']),
                stimulation2=Stimulation2.objects.create(**eval(data['hrv'])['stimulation2']),
                recovery2=Recovery2.objects.create(**eval(data['hrv'])['recovery2'])
            )
            eeg = EEG.objects.create()
            age = self.get_value(data, 'age')
            birth = self.get_value(data, 'birth')
            sex = self.get_value(data, 'sex')
            measurement_date = self.get_value(data, 'measurement_date')

            exp = Experiments(
                name=data['name'],
                age=age,
                birth=birth,
                sex=sex,
                measurement_date=measurement_date,
                hrv=hrv,
                eeg=eeg
            )
            exp.save()
            return Response(
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


class ExperimentListView(ListAPIView):
    pagination_class = ExperimentsPagination
    serializer_class = ExperimentsViewSerializer

    def get_queryset(self):
        queryset = Experiments.objects.filter()
        queryset = self.filter_queryset(queryset)
        return queryset

    def filter_queryset(self, queryset):
        name = self.request.GET.get('name')

        query = name
        if query:
            query_object = Q()
            if name:
                query_object.add(Q(name=name), Q.OR)
            queryset = queryset.filter(query_object)
        return queryset
