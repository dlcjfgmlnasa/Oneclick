# -*- coding:utf-8 -*-
from django.urls import path
from . import views


urlpatterns = [
    path('hrv/',
         views.HRVParameterGet.as_view(),
         name='subject add'),
    path('hrv/<pk>/',
         views.HRVParameterView.as_view(),
         name='subject veiw'),
]