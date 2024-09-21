from rest_framework.serializers import ModelSerializer
from .models import Anouncement, College

class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
        

class AnouncementSerializer(ModelSerializer):
    class Meta:
        model = Anouncement
        fields = '__all__' 
