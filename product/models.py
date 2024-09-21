from django.db import models
import uuid


# Product model
class Product(models.Model):

    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=200)
    product_description = models.CharField(max_length=500)
    product_features = models.CharField(max_length=5000)
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    availability_status = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    product_image = models.CharField(max_length=200)

    class Meta:
        db_table = "products"
