from rest_framework import viewsets
from cashback.sales import models
from cashback.sales.serializers import CostumerSerializer, ProductSerializer, CashBackSerializer


# Create your views here.



class CostumerViewSet(viewsets.ModelViewSet):
    queryset = models.Costumer.objects.all()
    serializer_class = CostumerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = ProductSerializer

class CashBackViewSet(viewsets.ModelViewSet):
    CASHBACK = {
        'A': 0.5,
        'B': 0.15,
    }
    queryset = models.CashBack.objects.all()
    serializer_class = CashBackSerializer





