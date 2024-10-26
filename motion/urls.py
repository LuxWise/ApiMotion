from rest_framework import routers
from .api import MotionViewSet

routers = routers.DefaultRouter()

routers.register('api/motion', MotionViewSet, 'motions')

urlpatterns = routers.urls
