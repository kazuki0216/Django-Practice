from django.db import models
from . import menu, customer

class DrinkSizeMetadata(models.TextChoices):
    SMALL = "SMALL", "Small"
    TALL = "TALL","Tall"
    GRANDE = "GRANDE", "Grande"
    VENTI = "VENTI", "Venti"

class DrinkType(models.TextChoices):
    HOT = "HOT", "Hot"
    COLD = "COLD", "Cold"

class Order(models.Model):
    menu_item = models.ForeignKey(menu.MenuItem, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer.Customer, on_delete=models.CASCADE)
    drink_type = models.CharField(max_length=5, choices=DrinkType.choices)
    size = models.CharField(max_length=128, choices=DrinkSizeMetadata.choices)
    ordered_at = models.DateTimeField(auto_now_add=True)
