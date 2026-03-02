from rest_framework import serializers
from .models import Movement

class MovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement
        fields = '__all__'
    
    def create(self, validated_data):
        movement = Movement(**validated_data)
        movement.save()
        return movement