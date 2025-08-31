from rest_framework import serializers

from ..models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    email = serializers.EmailField()

    class Meta:
        model = Customer
        unique_together = ("name", "email")
        fields = ["id", "name", "email", "phone_number", "created_at"]
