# -*- coding:utf-8 -*-
import os
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AppView(View):
    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR), 'backend', 'build', 'index.html'),
                      encoding='utf-8') as file:
                file = file.read()
                return HttpResponse(file)
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! build your react app!!
                """,
                status=501,
            )


class FlutterAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR), 'backend', 'build', 'flutter.js'),
                      encoding='utf-8') as file:
                file = file.read()
                return HttpResponse(file, content_type='application/javascript')
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! build your react app!!
                """,
                status=501,
            )


class FlutterWorkerView(View):
    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR), 'backend', 'build', 'flutter_service_worker.js'),
                      encoding='utf-8') as file:
                file = file.read()
                return HttpResponse(file, content_type='application/javascript')
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! build your react app!!
                """,
                status=501,
            )


class ManiFestView(View):
    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR), 'backend', 'build', 'manifest.json'),
                      encoding='utf-8') as file:
                file = file.read()
                return HttpResponse(file, content_type='application/json')
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! build your react app!!
                """,
                status=501,
            )


class DartAppView(View):
    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR), 'backend', 'build', 'main.dart.js'),
                      encoding='utf-8') as file:
                file = file.read()
                return HttpResponse(file, content_type='application/javascript')
        except FileNotFoundError:
            return HttpResponse(
                """
                index.html not found ! build your react app!!
                """,
                status=501,
            )