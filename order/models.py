from django.db import models
from user.models import User
import uuid


# Product model
class Order(models.Model):

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_date = models.CharField(max_length=200)
    total_price = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')

    class Meta:
        db_table = "order"
