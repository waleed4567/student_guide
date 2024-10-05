from users.views import UserSerializer
from .models import Article
from rest_framework.serializers import ModelSerializer

class ArticleSerializer(ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Article
        fields = '__all__' 


