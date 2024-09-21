from django.db import models
from product.models import Product
from order.models import Order
import uuid


# OrderItem model
class OrderItem(models.Model):

    order_item_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id')

    class Meta:
        db_table = "order_item"
