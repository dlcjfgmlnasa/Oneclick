"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import MyTokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    # JWT Token API
    path('api/v1/token-auth/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # REST API
    path('api/v1/exp/', include('experiments.urls')),
    path('api/v1/ecg/', include('ecg.urls')),
    path('api/v1/eeg/', include('eeg.urls')),
    path('api/v1/survey/', include('survey.urls'))

    # path('', views.AppView.as_view()),
    # path('flutter.js', views.FlutterAppView.as_view()),
    # path('manifest.json', views.ManiFestView.as_view()),
    # path('flutter_service_worker.js', views.FlutterWorkerView.as_view()),
    # path('main.dart.js', views.FlutterAppView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
