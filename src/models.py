from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)


class SubscriptionStatus(models.TextChoices):
    ACTIVE="ACTIVE", "Active"
    CANCELED="CANCELED", "Canceled"
    EXPIRED="EXPIRED", "Expired"

class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=128, choices=SubscriptionStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.TextField()
    available = models.BooleanField(default=True)

class DrinkSizeMetadata(models.TextChoices):
    SMALL = "SMALL", "Small"
    TALL = "TALL","Tall"
    GRANDE = "GRANDE", "Grande"
    VENTI = "VENTI", "Venti"

class DrinkType(models.TextChoices):
    HOT = "HOT", "Hot"
    COLD = "COLD", "Cold"

class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    drink_type = models.CharField(max_length=5, choices=DrinkType.choices)
    size = models.CharField(max_length=128, choices=DrinkSizeMetadata.choices)
    ordered_at = models.DateTimeField(auto_now_add=True)

class PaymentMethod(models.TextChoices):
    CASH = "CASH", "Cash"
    CREDIT = "CREDIT", "Credit"
    DEBIT = "DEBIT", "Debit"

class PaymentStatus(models.TextChoices):
    SUCCESS = "SUCCESS", "Success"
    FAILED = "FAILED", "Failed"
    PENDING = "PENDING", "Pending"

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=128, choices=PaymentMethod.choices)
    status = models.CharField(max_length=128, choices=PaymentStatus.choices)
