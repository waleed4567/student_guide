from rest_framework.serializers import ModelSerializer
from .models import Chapter, GuideTopic

class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
        

class GuideTopicSerializer(ModelSerializer):
    class Meta:
        model = GuideTopic
        fields = '__all__'
        