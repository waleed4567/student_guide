from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# User Serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff',)
        

# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

# Routes
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

