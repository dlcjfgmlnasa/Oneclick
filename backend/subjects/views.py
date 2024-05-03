# -*- coding:utf-8 -*-
from rest_framework.views import APIView
from rest_framework import status
from .models import Subject
from .serializer import SubjectSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q


class SubjectSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class SubjectView(APIView):
    def post(self, request):
        serializer_cls = SubjectSerializer(data=request.data)
        if serializer_cls.is_valid():
            serializer_cls.save()

            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_404_NOT_FOUND
        )


class SubjectListView(ListAPIView):
    pagination_class = SubjectSetPagination
    serializer_class = SubjectSerializer

    def get_queryset(self):
        queryset = Subject.objects.filter()
        queryset = self.filter_queryset(queryset)
        return queryset

    def filter_queryset(self, queryset):
        name = self.request.GET.get('name')

        query = name
        if query:
            query_object = Q()
            if name:
                query_object.add(Q(name=name), Q.OR)
            queryset = queryset.filter(query_object)
        return queryset

