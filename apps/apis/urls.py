
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Endpoints de autenticación
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Endpoints de la app transactions
    path('transactions/', include('apps.transactions.urls'), name='transactions'),
    # Endpoints de la app accounts
    path('accounts/', include('apps.accounts.urls'), name='accounts'),
    # Endpoints de la app reports
    path('reports/', include('apps.reports.urls'), name='reports'),
]