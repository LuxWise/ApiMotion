from rest_framework import serializers
from .models import Motion

class MotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motion
        fields = ('id', 'marca', 'sucursal', 'aspirante', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')