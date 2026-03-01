from rest_framework import serializers
from .models import Provider, Category, Product

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'
    
    def create(self, validated_data):
        provider = Provider(**validated_data)
        provider.save()
        return provider
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
    def create(self, validated_data):
        category = Category(**validated_data)
        category.save()
        return category
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product