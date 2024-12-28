from django.urls import path
from .apis.views.login import CustomTokenObtainPairView
from .apis.views.register import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
