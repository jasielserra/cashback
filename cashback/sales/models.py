from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
# Create your models here.

class Costumer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Costumer"))
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    document = models.CharField(verbose_name=_("CPF"), max_length=11, validators=[MinLengthValidator(11)])


class Product(models.Model):
    type = models.PositiveSmallIntegerField(null=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    qty = models.PositiveSmallIntegerField(null=False)


class CashBack(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,)
    sold_at = models.DateTimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)