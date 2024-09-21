from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import OfficeSerializer
from .models import Office

class UnitViewSet(ModelViewSet):
    serializer_class = OfficeSerializer
    queryset = Office.objects.all()
    

