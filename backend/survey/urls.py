# -*- coding:utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.QuestionnaireListView.as_view(),
        name='list questionnaire'
    ),
    path(
        'questionnaire/<pk>/',
        views.QuestionnaireView.as_view(),
        name='list questionnaire'
    ),
]
