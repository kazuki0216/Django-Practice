from django.db import models
from . import customer

class SubscriptionStatus(models.TextChoices):
    ACTIVE="ACTIVE", "Active"
    CANCELED="CANCELED", "Canceled"
    EXPIRED="EXPIRED", "Expired"

class Subscription(models.Model):
    customer = models.ForeignKey(customer.Customer, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=128, choices=SubscriptionStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
