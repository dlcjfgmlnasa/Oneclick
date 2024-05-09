# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from subjects.models import Subject
from subjects.serializer import SubjectSerializer
from ecg.serializer import *
from ecg.models import HRV, Baseline, Stimulation1, Recovery1, Stimulation2, Recovery2


class HRVParameterGet(APIView):
    def post(self, requests):
        try:
            sample = eval(str(requests.data['data']))
            subject_obj = Subject.objects.get_or_create(**sample['subject'])[0]
            baseline_obj = Baseline.objects.create(**sample['stimulation1'])
            stimulation1_obj = Stimulation1.objects.create(**sample['stimulation1'])
            recovery1_obj = Recovery1.objects.create(**sample['recovery1'])
            stimulation2_obj = Stimulation2.objects.create(**sample['stimulation2'])
            recovery2_obj = Recovery2.objects.create(**sample['recovery2'])

            hrv = HRV.objects.create(
                subject=subject_obj,
                measurement_date=sample['measurement_date'],
                baseline=baseline_obj,
                stimulation1=stimulation1_obj,
                recovery1=recovery1_obj,
                stimulation2=stimulation2_obj,
                recovery2=recovery2_obj
            )
            serializer_cls = HRVSerializer(hrv)
            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                data={'error': 'contact server administrator'},
                status=status.HTTP_400_BAD_REQUEST
            )


class HRVParameterView(APIView):
    @staticmethod
    def get_hrv(pk):
        try:
            model = HRV.objects.get(pk=pk)
            return model
        except HRV.DoesNotExist:
            return None

    def get(self, requests, pk):
        hrv = self.get_hrv(pk)
        if hrv is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer_cls = HRVSerializer(hrv)
        return Response(
            serializer_cls.data,
            status=status.HTTP_200_OK
        )

