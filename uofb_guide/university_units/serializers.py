from .models import Office
from rest_framework.serializers import ModelSerializer

class OfficeSerializer(ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__' 
