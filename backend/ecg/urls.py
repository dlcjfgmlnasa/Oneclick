# -*- coding:utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('hrv/<pk>/',
         views.HRVParameterView.as_view(),
         name='subject pk'),
]