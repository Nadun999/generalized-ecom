from django.http import JsonResponse
from .models import OrderItem
from .serializers import OrderItemSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def create_order_item(request):

    if request.method == 'GET':
        order_item = OrderItem.objects.all()
        serializer = OrderItemSerializer(order_item, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
