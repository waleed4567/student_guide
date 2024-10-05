from django.urls import path
from rest_framework import routers
from .views import ArticleViewSet

news_route = routers.DefaultRouter()
news_route.register('article', ArticleViewSet)

urlpatterns = [
    
]
