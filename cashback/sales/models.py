from django.db import models
from cashback import settings
# Create your models here.



class Costumer(models.Model):
    user = models.CharField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=("Name"), max_length=50)
    document = models.CharField(verbose_name=("CPF"), max_length=11)


class Product(models.Model):
    type = models.PositiveSmallIntegerField(null=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    qty = models.PositiveSmallIntegerField(null=False)


class CashBack(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,)
    sold_at = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)