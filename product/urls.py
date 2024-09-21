from django.urls import path
from .views import product_handle, specific_product_handle, get_product_by_category, get_product_by_subcategory, \
    upload_product_img

urlpatterns = [
    path('products/', product_handle, name='product_handler'),
    path('products/<str:product_id>', specific_product_handle, name='specific_product_handler'),
    path('products/category/<str:category>', get_product_by_category, name='get_product_by_category'),
    path('products/sub-category/<str:sub_category>', get_product_by_subcategory, name='get_product_by_subcategory'),
    path('products/img/', upload_product_img, name='upload_product_img'),
]
