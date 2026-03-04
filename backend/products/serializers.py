from rest_framework import serializers
from .models import Product
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product