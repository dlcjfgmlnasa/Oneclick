# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from report.models import Report
from experiments.models import Experiments
from experiments.serializer import ExperimentsQuestionnaireSerializer
from report.serializer import ReportSerializer

class SleepReportListView(APIView):
    @staticmethod
    def get_sleepreport(pk):
        try:
            model = Report.objects.get(pk=pk)
            return model
        except Report.DoesNotExist:
            return None

    def get(self, requests, pk):
        sleep_report = self.get_sleepreport(pk)
        if sleep_report is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = ReportSerializer(sleep_report)
        data = serializer_cls.data
        return Response(
            data,
            status=status.HTTP_200_OK
        )

