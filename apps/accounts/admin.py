from django.contrib import admin

from .models import PaymentConfig
from .models import User


admin.site.register(PaymentConfig)
admin.site.register(User)
