# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from eeg.serializer import EEGSerializer
from eeg.models import EEG


class EEGParameterView(APIView):
    @staticmethod
    def get_eeg(pk):
        try:
            model = EEG.objects.get(pk=pk)
            return model
        except EEG.DoesNotExist:
            return None

    def get(self, requests, pk):
        eeg = self.get_eeg(pk)
        if eeg is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = EEGSerializer(eeg)
        data = serializer_cls.data
        return Response(
            data,
            status=status.HTTP_200_OK
        )
