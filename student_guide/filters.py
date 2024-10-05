import django_filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from .models import GuideTopic, Chapter

class TopicFilter(DjangoFilterBackend):
    pass

    # class Meta:
    #     model = GuideTopic
    #     fields = ['id', 'title', 'ar_title', 'chapter', 'created', 'updated', 'content', 'ar_content',]
        
