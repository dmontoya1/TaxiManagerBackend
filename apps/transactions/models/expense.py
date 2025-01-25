
from django.conf import settings
from django.db import models

from apps.transactions.models.transaction import Transaction

class Expense(Transaction):
    category = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses', null=True)

    def __str__(self):
        return f'Gasto de {self.amount} del {self.date} en {self.category}'

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-date']
