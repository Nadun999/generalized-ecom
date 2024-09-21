from django.db import models
import uuid


# User model
class User(models.Model):

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    user_level = models.CharField(max_length=200)

    class Meta:
        db_table = "user"
