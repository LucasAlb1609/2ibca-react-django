from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserRegistrationSerializer, MyTokenObtainPairSerializer


from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    """
    View de login que usa nosso serializer de token personalizado.
    """
    serializer_class = MyTokenObtainPairSerializer

class UserRegisterView(generics.CreateAPIView):
    """ View de API para registrar um novo usuário (cadastro). """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

class DashboardStatsAPIView(APIView):
    """ View de API que retorna estatísticas do sistema para o dashboard do secretário. """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if not request.user.is_secretario:
            return Response(
                {"detail": "Acesso negado. Apenas secretários podem ver as estatísticas."},
                status=status.HTTP_403_FORBIDDEN
            )
        stats = {
            'total_usuarios': User.objects.count(),
            'usuarios_pendentes': User.objects.filter(aprovado=False).count(),
            'total_membros': User.objects.filter(papel='membro', aprovado=True).count(),
            'total_congregados': User.objects.filter(papel='congregado', aprovado=True).count(),
        }
        return Response(stats)