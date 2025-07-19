from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

