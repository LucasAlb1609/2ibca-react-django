from django.urls import path
from .views import ConfiguracaoSiteAPIView, DevocionalRecenteAPIView

urlpatterns = [
    path('configuracao/', ConfiguracaoSiteAPIView.as_view(), name='api-configuracao'),
    path('devocionais/recente/', DevocionalRecenteAPIView.as_view(), name='api-devocional-recente'),
]