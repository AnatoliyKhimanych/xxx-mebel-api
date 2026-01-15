from rest_framework import generics
from .models import Furniture, Order
from .serializers import FurnitureSerializer, OrderSerializer
from rest_framework.response import Response


class FurnitureListView(generics.ListAPIView):
  queryset = Furniture.objects.all()
  serializer_class = FurnitureSerializer


class FurnitureDetailView(generics.RetrieveAPIView):
  queryset = Furniture.objects.all()
  serializer_class = FurnitureSerializer


class OrderCreateView(generics.CreateAPIView):
  queryset = Order.objects.all()
  serializer_class = OrderSerializer

  def perform_create(self, serializer):
    items = serializer.validated_data['items']
    total = sum(item.price for item in items)
    serializer.save(total_price=total)


class OrderListByEmailView(generics.ListAPIView):
  serializer_class = OrderSerializer

  def get_queryset(self):
    email = self.request.query_params.get('email')
    return Order.objects.filter(email=email)

