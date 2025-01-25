from django.urls import path
from .apis.views.login import CustomTokenObtainPairView
from .apis.views.register import RegisterView
from .apis.views.validate_token import ValidateTokenView
from .apis.views.payment_config import PaymentConfigView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('validate-token/', ValidateTokenView.as_view(), name='validate_token'),
    path('payment-config/', PaymentConfigView.as_view(), name='payment_config'),
]
