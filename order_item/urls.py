from django.urls import path
from .views import create_order_item

urlpatterns = [
    path('order_items/', create_order_item, name='create_order_item'),
]
