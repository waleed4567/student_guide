from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import EventSerializer
from .models import Event

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    

