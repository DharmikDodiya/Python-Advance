from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    def validate(self, value):
        if value['stock'] == 0 and value['price'] > 0:
            raise serializers.ValidationError("Cannot set a price if stock is zero.")
        return value