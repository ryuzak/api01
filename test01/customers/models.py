from django.db import models

from accounts.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    class Meta:
        db_table = 'customers'

