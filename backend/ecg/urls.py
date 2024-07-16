# -*- coding:utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('hrv/<pk>/',
         views.HRVParameterView.as_view(),
         name='subject pk'),
    path('hrv/<pk>/note/',
         views.HRVNoteView.as_view(),
         name='subject note pk')
]
