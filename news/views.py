#from typing import override
from urllib import request
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters
from django_filters import CharFilter

from college.models import College
from .models import Article
from .serializers import ArticleSerializer
from django.db.models.query import QuerySet


# TODO Declare a Search for News Article Then redo it in other models
class ArticleViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, filters.SearchFilter):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    search_fields = ['id', 'title', 'content']
    


    
    
    
    
