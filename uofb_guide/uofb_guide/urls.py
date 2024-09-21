from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from university_units.views import UnitViewSet
from news.views import ArticleViewSet
from student_guide.views import GuideViewSet, WebIndex
from college.views import AnouncementViewSet, CollegeViewSet
from year_calendar.views import EventViewSet
from users.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'guide', GuideViewSet) # Guide Entries
# router.register(r'units', UnitViewSet) # University Units
router.register(r'anouncements', AnouncementViewSet) # Anouncements
router.register(r'Colleges', CollegeViewSet) # Colleges
router.register(r'calendar', EventViewSet)# All Calendar Events 
router.register(r'news', ArticleViewSet) # News
router.register(r'users', UserViewSet)# Users Views

urlpatterns = [
    path('', WebIndex.as_view(), name="Home Page"),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('colleges/', include('college.urls')),
    # path('calendar', include('year_calendar.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
] #+ router.urls



from django.contrib import admin

admin.site.site_header = 'Student Guide'                    # default: "Django Administration"
admin.site.index_title = 'Student Guide'                 # default: "Site administration"
admin.site.site_title = 'Student Guide Admin' # default: "Django site admin"
