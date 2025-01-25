from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class User(AbstractUser):
    ROLE_CHOICES = [
        ('driver', 'Taxista'),
        ('boss', 'Jefe'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='driver')
    phone = models.CharField(max_length=15, blank=True, null=True)
    boss = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='drivers')

    def is_driver(self):
        return self.role == 'driver'

    def is_boss(self):
        return self.role == 'boss'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class PaymentConfig(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payment_config')
    is_percentage = models.BooleanField(default=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Configuración de pago para {self.user.username}"

    class Meta:
        verbose_name = "Configuración de Pago"
        verbose_name_plural = "Configuraciones de Pago"
