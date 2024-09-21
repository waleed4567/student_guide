from typing import override
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .models import Anouncement, College
from .serializers import AnouncementSerializer, CollegeSerializer

class CollegeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()


class AnouncementViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = AnouncementSerializer
    queryset = Anouncement.objects.all() # filtered_queryset() #
    
    @override
    def list(self, request, *args, **kwargs):
        # queryset = self.filter_queryset(self.get_queryset())
        college = request.GET.get('college') or 1
        college = College.objects.get(pk=college)
        queryset = Anouncement.objects.filter(college=college)
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
