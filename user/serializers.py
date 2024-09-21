from rest_framework import serializers
from .models import User
from order.serializers import OrderSerializer


# User model serializer
class UserSerializer(serializers.ModelSerializer):

    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'email', 'password', 'user_level', 'orders']
