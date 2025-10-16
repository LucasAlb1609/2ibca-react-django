from django.urls import path
from .views import UserRegisterView, DashboardStatsAPIView

urlpatterns = [

    path('auth/register/', UserRegisterView.as_view(), name='api-register'),
    path('admin/dashboard-stats/', DashboardStatsAPIView.as_view(), name='api-dashboard-stats'),
]
