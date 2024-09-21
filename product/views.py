import os
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def product_handle(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def specific_product_handle(request, product_id):
    print('method executed')
    if request.method == 'GET':
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_product_by_category(request, category):
    if request.method == 'GET':
        try:
            product = Product.objects.filter(category=category)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['GET'])
def get_product_by_subcategory(request, sub_category):
    if request.method == 'GET':
        try:
            product = Product.objects.filter(sub_category=sub_category)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['POST'])
def upload_product_img(request):
    if request.method == 'POST':
        product_img = request.FILES['image']
        upload_dir = f'product/main/temp/'

        # Create the directory if it doesn't exist
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Save the image to the specified directory
        fs = FileSystemStorage(location=upload_dir)
        file_name = fs.save(product_img.name, product_img)

        return Response(file_name, status=status.HTTP_201_CREATED)
