from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from apps.transactions.models import Income, Expense
from django.db.models import Sum, Q
from datetime import datetime, timedelta
from apps.accounts.models import PaymentConfig

class ReportsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Obtener parámetros de fecha
        date_str = request.query_params.get("date", None)
        start_date_str = request.query_params.get("start_date", None)
        end_date_str = request.query_params.get("end_date", None)

        # Convertir fechas a objetos datetime
        date = datetime.strptime(date_str, "%Y-%m-%d").date() if date_str else None
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date() if start_date_str else None
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date() if end_date_str else None

        # Obtener ingresos y gastos del usuario
        if user.is_boss():
            incomes = Income.objects.filter(user__boss=user)
            expenses = Expense.objects.filter(user__boss=user)
        else:
            incomes = Income.objects.filter(user=user)
            expenses = Expense.objects.filter(user=user)

        # Filtrar por fecha
        if date:
            incomes = incomes.filter(date=date)
            expenses = expenses.filter(date=date)
        elif start_date and end_date:
            incomes = incomes.filter(date__range=[start_date, end_date])
            expenses = expenses.filter(date__range=[start_date, end_date])

        # Calcular totales
        total_incomes = incomes.aggregate(total=Sum('amount'))['total'] or 0
        total_expenses = expenses.aggregate(total=Sum('amount'))['total'] or 0

        # Calcular pagos en efectivo y tarjeta
        cash_incomes = incomes.filter(payment_method='cash').aggregate(total=Sum('amount'))['total'] or 0
        card_incomes = incomes.filter(payment_method='card').aggregate(total=Sum('amount'))['total'] or 0

        # Obtener configuración de pagos al jefe
        config, created = PaymentConfig.objects.get_or_create(
            user=user,
            defaults={'is_percentage': True, 'value': 0.0}
        )

        # Calcular pago al jefe y ganancias del conductor
        if config.is_percentage:
            payment_to_boss = total_incomes * (config.value / 100)
        else:
            payment_to_boss = config.value

        driver_earnings = total_incomes - payment_to_boss

        # Respuesta con los totales y detalles
        response = {
            "incomes": {
                "total": total_incomes,
                "cash": cash_incomes,
                "card": card_incomes,
            },
            "expenses": {
                "total": total_expenses,
            },
            "payment_to_boss": payment_to_boss,
            "driver_earnings": driver_earnings,
        }

        return Response(response, status=status.HTTP_200_OK)
