
from django.conf import settings
from django.db import models

from apps.transactions.models.transaction import Transaction


class Income(Transaction):
    PAYMENT_METHODS = [
        ('cash', 'Efectivo'),
        ('card', 'Tarjeta'),
    ]
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='incomes', null=True)

    def __str__(self):
        return f'Ingreso de {self.amount} del {self.date} por {self.payment_method}'

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
