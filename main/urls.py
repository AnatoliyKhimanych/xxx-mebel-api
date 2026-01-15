from django.urls import path
from .views import (
  FurnitureListView,
  FurnitureDetailView,
  OrderCreateView,
  OrderListByEmailView
)

urlpatterns = [
  path('furniture/', FurnitureListView.as_view()),
  path('furniture/<int:pk>/', FurnitureDetailView.as_view()),
  path('orders/', OrderCreateView.as_view()),
  path('orders/list/', OrderListByEmailView.as_view()),
]
