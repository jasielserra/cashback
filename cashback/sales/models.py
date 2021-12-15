from django.utils import timezone
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.

class Costumer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Costumer"))
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    document = models.CharField(verbose_name=_("CPF"), max_length=11, validators=[MinLengthValidator(11)])

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.PositiveSmallIntegerField(null=False, verbose_name=_("Type"), default=0)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name=_("Value"))
    qty = models.PositiveSmallIntegerField(null=False, verbose_name=_("Quantity"))


class CashBack(models.Model):
    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE, verbose_name=_("Customer"))
    products = models.ManyToManyField(Product, verbose_name=_("Products"))
    sold_at = models.DateTimeField(default=timezone.now, verbose_name=_("Sale Date"))
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name=_("Total"))

    def __str__(self):
        return self.costumer.name + " | " + str(self.total)

    def sanitize(self):
        if self.total < 0:
            raise ValidationError("Cannot be negative")