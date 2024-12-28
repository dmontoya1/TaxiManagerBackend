from django.db import models

class Transaction(models.Model):
    date = models.DateField(auto_now_add=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True
