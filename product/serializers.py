from rest_framework import serializers
from .models import Product
from order_item.serializers import OrderItemSerializer


# Product model serializer
class ProductSerializer(serializers.ModelSerializer):

    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'product_description', 'product_features', 'product_price',
                  'availability_status', 'category', 'sub_category', 'product_image', 'order_items']
