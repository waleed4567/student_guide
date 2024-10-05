from rest_framework.serializers import ModelSerializer
from .models import Chapter, GuideTopic

class ChapterSerializer(ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
        

class GuideTopicSerializer(ModelSerializer):
    chapter = ChapterSerializer()
    class Meta:
        model = GuideTopic
        fields = '__all__'#['id', 'title', 'ar_title', 'chapter', 'created', 'updated', 'content', 'ar_content', 'image']
        