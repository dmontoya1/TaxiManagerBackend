
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ...models import Income
from ...permissions import IsBossOrDriver
from .serializer import IncomeSerializer


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.all().order_by('-date')
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsBossOrDriver]

    def get_queryset(self):
        # Filtrar los ingresos solo del usuario autenticado
        user = self.request.user
        if user.is_boss():
            # El jefe puede ver los ingresos de sus taxistas
            return Income.objects.filter(user__boss=user)
        else:
            # El taxista solo puede ver sus propios ingresos
            return Income.objects.filter(user=user)

    def perform_create(self, serializer):
        # Asignar automáticamente el usuario autenticado al ingreso
        serializer.save(user=self.request.user)
