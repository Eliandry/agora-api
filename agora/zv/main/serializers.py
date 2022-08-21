from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.Serializer):
    product_id = serializers.CharField(max_length=120)
    name = serializers.CharField(max_length=1000)
    reference_id = serializers.CharField(max_length=120)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)