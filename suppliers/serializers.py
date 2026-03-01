from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
    
    def create(self, validated_data):
        supplier = Supplier(**validated_data)
        supplier.save()
        return supplier