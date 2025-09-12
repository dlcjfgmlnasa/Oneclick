# -*- coding:utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path(
        '<pk>/',
        views.SleepReportListView.as_view(),
        name='list sleepreport'
    ),
]