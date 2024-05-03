# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.SubjectView.as_view(),
         name='subject add'),
    path('list/',
         views.SubjectListView.as_view(),
         name='subject list'),
]