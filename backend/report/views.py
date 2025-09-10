# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from report.models import Report
from experiments.models import Experiments
from experiments.serializer import ExperimentsQuestionnaireSerializer
from report.serializer import ReportSerializer


#It won't be neccessary now