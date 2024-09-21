from rest_framework import serializers
from .models import Order
from order_item.serializers import OrderItemSerializer


# User model serializer
class OrderSerializer(serializers.ModelSerializer):

    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'order_date', 'total_price', 'status', 'address', 'number', 'user_id', 'order_items']
