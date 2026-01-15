from rest_framework import serializers
from .models import Furniture, Order


class FurnitureSerializer(serializers.ModelSerializer):
  class Meta:
    model = Furniture
    fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
  items = serializers.PrimaryKeyRelatedField(
    queryset=Furniture.objects.all(),
    many=True
  )

  class Meta:
    model = Order
    fields = ['id', 'email', 'items', 'total_price', 'created_at']
    read_only_fields = ['total_price', 'created_at']
