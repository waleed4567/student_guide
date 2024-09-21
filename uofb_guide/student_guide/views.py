from typing import override
from django.shortcuts import render
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import SearchFilter

from .models import Chapter, GuideTopic
from .serializers import ChapterSerializer, GuideTopicSerializer


class GuideViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, SearchFilter):
    serializer_class = GuideTopicSerializer
    queryset = GuideTopic.objects.filter(chapter__number=1) # Filter to return topics with specific chapter number
    authentication_classes = []
    search_param = 'q'
    search_fields = ['id', 'title', 'content', 'chapter__name']
    
    @override
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)   


class ChaptersViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, SearchFilter):
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
    authentication_classes = []
    
    @override
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    
class WebIndex(View):
    def get(self, request):
        return render(request, 'index.html')