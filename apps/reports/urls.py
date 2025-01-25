from django.urls import path
from .apis.views.reports import ReportsView

urlpatterns = [
    path('', ReportsView.as_view(), name='reports'),
]