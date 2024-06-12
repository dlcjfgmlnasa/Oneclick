# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .serializer import ExperimentsViewSerializer
from .models import Experiments
from ecg.models import *
from eeg.models import *
from django.db.models import Q
from PIL import Image
import base64
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


class ExperimentsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ExperimentView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get_value(data, param_name):
        try:
            value = data[param_name]
        except KeyError:
            value = None
        return value

    @staticmethod
    def base64_file(data, name=None):
        from uuid import uuid4
        from django.core.files.base import ContentFile
        name = str(uuid4())
        return ContentFile(base64.b64decode(data), name='{}'.format(name))

    def image_obj_save(self, obj, name, contents):
        eeg = obj.objects.create(
            topography_delta=self.base64_file(contents[name]['topography_delta']),
            topography_theta=self.base64_file(contents[name]['topography_theta']),
            topography_alpha=self.base64_file(contents[name]['topography_alpha']),
            topography_beta=self.base64_file(contents[name]['topography_beta']),
            topography_gamma=self.base64_file(contents[name]['topography_gamma']),
            connectivity_delta=self.base64_file(contents[name]['connectivity_delta']),
            connectivity_theta=self.base64_file(contents[name]['connectivity_theta']),
            connectivity_alpha=self.base64_file(contents[name]['connectivity_alpha']),
            connectivity_beta=self.base64_file(contents[name]['connectivity_beta']),
            connectivity_gamma=self.base64_file(contents[name]['connectivity_gamma'])
        )
        return eeg

    def post(self, request):
        data = request.data

        try:
            hrv = HRV.objects.create(
                nni=eval(data['hrv'])['nni'],
                rmssd=eval(data['hrv'])['rmssd'],
                baseline=HRVBaseline.objects.create(**eval(data['hrv'])['baseline']),
                stimulation1=HRVStimulation1.objects.create(**eval(data['hrv'])['stimulation1']),
                recovery1=HRVRecovery1.objects.create(**eval(data['hrv'])['recovery1']),
                stimulation2=HRVStimulation2.objects.create(**eval(data['hrv'])['stimulation2']),
                recovery2=HRVRecovery2.objects.create(**eval(data['hrv'])['recovery2'])
            )

            eeg = EEG.objects.create(
                psd=eval(data['eeg'])['psd'],
                sleep_staging=eval(data['eeg'])['sleep_staging'],
                baseline=self.image_obj_save(EEGBaseline, 'baseline', eval(data['eeg'])),
                stimulation1=self.image_obj_save(EEGStimulation1, 'stimulation1', eval(data['eeg'])),
                recovery1=self.image_obj_save(EEGRecovery1, 'recovery1', eval(data['eeg'])),
                stimulation2=self.image_obj_save(EEGStimulation2, 'stimulation2', eval(data['eeg'])),
                recovery2=self.image_obj_save(EEGRecovery2, 'recovery2', eval(data['eeg'])),
            )

            age = self.get_value(data, 'age')
            birth = self.get_value(data, 'birth')
            sex = self.get_value(data, 'sex')
            measurement_date = self.get_value(data, 'measurement_date')

            exp = Experiments(name=data['name'], age=age, birth=birth, sex=sex,
                              measurement_date=measurement_date,
                              hrv=hrv,
                              eeg=eeg)
            exp.save()
            return Response(
                {'result': 'Success!!'},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {'result': 'Failed!! Contact Your Administrator!!'},
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
