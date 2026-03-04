from rest_framework.serializers import ModelSerializer
from .models import CustomUser
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['username', 'email', 'password']
    
    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.password = make_password(user.password)
        user.is_superuser = True
        user.save()
        return user