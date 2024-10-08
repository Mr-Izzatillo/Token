from .models import Order
from rest_framework import serializers

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model= Order
        fields = ['qty', 'user', 'product', 'price', 'created_at', 'address', 'phone_number', 'description', 'status']