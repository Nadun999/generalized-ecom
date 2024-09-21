from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('product.urls')),
    path('v1/', include('user.urls')),
    path('v1/', include('order.urls')),
    path('v1/', include('order_item.urls')),
]
