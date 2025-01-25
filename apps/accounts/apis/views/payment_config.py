from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ...models import PaymentConfig
from ..serializers.payment_config import PaymentConfigSerializer


class PaymentConfigView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Obtener o crear la configuración con valores predeterminados
        config, created = PaymentConfig.objects.get_or_create(
            user=request.user,
            defaults={'is_percentage': True, 'value': 0.0}  # Valores predeterminados
        )
        serializer = PaymentConfigSerializer(config)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Obtener o crear la configuración con valores predeterminados
        config, created = PaymentConfig.objects.get_or_create(
            user=request.user,
            defaults={'is_percentage': True, 'value': 0.0}  # Valores predeterminados
        )
        serializer = PaymentConfigSerializer(config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)