# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ecg.models import HRV, Baseline, Stimulation1, Recovery1, Stimulation2, Recovery2
from ecg.serializer import *


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

