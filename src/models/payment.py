from django.db import models
from . import customer


class PaymentMethod(models.TextChoices):
    CASH = "CASH", "Cash"
    CREDIT = "CREDIT", "Credit"
    DEBIT = "DEBIT", "Debit"

class PaymentStatus(models.TextChoices):
    SUCCESS = "SUCCESS", "Success"
    FAILED = "FAILED", "Failed"
    PENDING = "PENDING", "Pending"

class Payment(models.Model):
    customer = models.ForeignKey(customer.Customer, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=128, choices=PaymentMethod.choices)
    status = models.CharField(max_length=128, choices=PaymentStatus.choices)
