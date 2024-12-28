from rest_framework import serializers
from ...models import Income


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'amount', 'payment_method', 'description', 'date']
        read_only_fields = ['id',]
