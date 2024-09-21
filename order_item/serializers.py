from rest_framework import serializers
from .models import OrderItem


# User model serializer
class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['order_item_id', 'quantity', 'price', 'product_id', 'order_id']
