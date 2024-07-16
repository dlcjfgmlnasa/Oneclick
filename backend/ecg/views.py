# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
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
        data = serializer_cls.data
        return Response(
            data,
            status=status.HTTP_200_OK
        )


class HRVNoteView(APIView):
    @staticmethod
    def get_hrv(pk):
        try:
            model = HRV.objects.get(pk=pk)
            return model
        except HRV.DoesNotExist:
            return None

    def put(self, requests, pk):
        hrv = self.get_hrv(pk)
        if hrv is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = HRVNoteSerializer(hrv, data=requests.data)
        if serializer_cls.is_valid():
            serializer_cls.save()
            return Response(
                data=serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
