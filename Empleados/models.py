from django.db import models
from django.contrib.auth.models import AbstractUser
from Clientes.models import BarberShop

class CustomUser(AbstractUser):
    barber_shop = models.ForeignKey(BarberShop, on_delete=models.SET_NULL, null=True, blank=True)

