# -*- coding:utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('analysis/<pk>/',
         views.EEGParameterView.as_view(),
         name='subject pk'),
]