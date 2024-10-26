from .models import Motion
from rest_framework import viewsets, permissions
from .serializers import MotionSerializer

class MotionViewSet(viewsets.ModelViewSet):
    queryset = Motion.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MotionSerializer