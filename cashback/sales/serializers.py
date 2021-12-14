import models
from rest_framework import serializers

class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Customer
        fields = ['user', 'document', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['type', 'value', 'qty']

class CashBackSerializer(serializers.ModelSerializer):
    costumer = CostumerSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        models = models.CashBack
        fields = ['sold_at', 'total', 'customer', 'products']