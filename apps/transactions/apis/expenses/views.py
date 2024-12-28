
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ...models import Expense
from ...permissions import IsBossOrDriver
from .serializer import ExpenseSerializer

class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsBossOrDriver]
    ordering = ['-date']

    def get_queryset(self):
        user = self.request.user
        if user.is_boss():
            return Expense.objects.filter(user__boss=user)
        else:
            return Expense.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
