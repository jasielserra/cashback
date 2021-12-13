from django.db import models
from cashback import settings
# Create your models here.



class costumer(models.Model):
    user = models.CharField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=("Costumer"))
    name = models.CharField(verbose_name=("Name"), max_length=50)
    document = models.CharField(verbose_name=("CPF"), max_length=11)