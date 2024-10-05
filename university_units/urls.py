from django.urls import path
from .views import UnitViewSet

urlpatterns = [
    path('', UnitViewSet.as_view({'get': 'list', 'post': 'create'})),
]
