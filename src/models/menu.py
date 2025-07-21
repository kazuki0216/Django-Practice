from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.TextField()
    available = models.BooleanField(default=True)
