from rest_framework import serializers

from ..models import Menu


class MenuSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    description = serializers.CharField(max_length=200)
    available = serializers.BooleanField()

    class Meta:
        model = Menu
        fields = ["id", "name", "price", "description", "available"]
