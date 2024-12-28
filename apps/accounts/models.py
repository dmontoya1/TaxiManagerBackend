from django.contrib.auth.models import AbstractUser
from django.db import models


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