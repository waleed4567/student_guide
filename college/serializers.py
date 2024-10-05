from rest_framework.serializers import ModelSerializer
from .models import Anouncement, College
from django.contrib.auth.models import User


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'
        

class AnouncementSerializer(ModelSerializer):
    college = CollegeSerializer()
    class Meta:
        model = Anouncement
        fields = '__all__' 
