from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apis.incomes.views import IncomeViewSet
from .apis.expenses.views import ExpenseViewSet

router = DefaultRouter()
router.register('incomes', IncomeViewSet, basename='income')
router.register('expenses', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('', include(router.urls)),
]