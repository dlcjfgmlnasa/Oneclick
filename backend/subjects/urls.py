# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path('list/',
         views.AccountListView.as_view(),
         name='subject list'),
]