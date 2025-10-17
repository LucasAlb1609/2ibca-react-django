from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from .models import User
from .permissions import IsSecretario
from .serializers import (
    UserRegistrationSerializer, MyTokenObtainPairSerializer, UserProfileSerializer, UserProfileUpdateSerializer, AdminUserListSerializer, AdminUserCreateSerializer, 
    AdminUserUpdateSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


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

class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    View de API para LER ou ATUALIZAR os dados do usuário logado.
    GET: Retorna o perfil (usa UserProfileSerializer).
    PUT/PATCH: Atualiza o perfil (usa UserProfileUpdateSerializer).
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        # Usa um serializer diferente para leitura (GET) e escrita (PUT/PATCH)
        if self.request.method == 'GET':
            return UserProfileSerializer
        return UserProfileUpdateSerializer

    def get_object(self):
        return self.request.user
    
class AdminUserListView(generics.ListCreateAPIView):
    """
    View de API para secretários LISTAREM (GET com filtros) e CRIAREM (POST) usuários.
    """
    queryset = User.objects.all().order_by('nome_completo')
    permission_classes = [IsAuthenticated, IsSecretario]
    
    # Configuração dos filtros
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['papel', 'aprovado', 'ativo'] # Campos para filtro exato (ex: /api/admin/users/?papel=membro)
    search_fields = ['nome_completo', 'email', 'cpf'] # Campos para busca textual (ex: /api/admin/users/?search=João)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AdminUserCreateSerializer
        return AdminUserListSerializer

class AdminPendingUserListView(generics.ListAPIView):
    queryset = User.objects.filter(aprovado=False).order_by('data_cadastro')
    serializer_class = AdminUserListSerializer
    permission_classes = [IsAuthenticated, IsSecretario]

class AdminApproveUserView(APIView):
    permission_classes = [IsAuthenticated, IsSecretario]
    def post(self, request, pk, format=None):
        try:
            user_to_approve = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        new_role = request.data.get('papel')
        if new_role not in ['membro', 'congregado', 'secretario']:
            return Response({"detail": "Papel inválido fornecido."}, status=status.HTTP_400_BAD_REQUEST)
        user_to_approve.aprovado = True
        user_to_approve.aprovado_por = request.user
        user_to_approve.data_aprovacao = timezone.now()
        user_to_approve.papel = new_role
        user_to_approve.save()
        return Response({"detail": f"Usuário {user_to_approve.nome_completo} aprovado como {user_to_approve.get_papel_display()}."}, status=status.HTTP_200_OK)

class AdminRejectUserView(APIView):
    permission_classes = [IsAuthenticated, IsSecretario]
    def delete(self, request, pk, format=None):
        try:
            user_to_reject = User.objects.get(pk=pk, aprovado=False)
        except User.DoesNotExist:
            return Response({"detail": "Usuário pendente não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        user_to_reject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AdminUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View de API para um secretário:
    - LER (GET) os detalhes completos de um usuário.
    - ATUALIZAR (PUT/PATCH) os dados de um usuário.
    - EXCLUIR (DELETE) um usuário.
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsSecretario]

    def get_serializer_class(self):
        # Usa um serializer para leitura e outro para escrita
        if self.request.method in ['PUT', 'PATCH']:
            return AdminUserUpdateSerializer
        return UserProfileSerializer

class AdminPendingUserListView(generics.ListAPIView):
    """
    View de API para secretários listarem apenas usuários pendentes de aprovação.
    """
    # Filtra o queryset para pegar apenas usuários não aprovados
    queryset = User.objects.filter(aprovado=False).order_by('data_cadastro')
    serializer_class = AdminUserListSerializer # Reutilizamos o serializer da lista
    permission_classes = [IsAuthenticated, IsSecretario]

class AdminApproveUserView(APIView):
    """
    View de API para um secretário aprovar um usuário e definir seu papel.
    """
    permission_classes = [IsAuthenticated, IsSecretario]

    def post(self, request, pk, format=None):
        try:
            user_to_approve = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"detail": "Usuário не encontrado."}, status=status.HTTP_404_NOT_FOUND)

        new_role = request.data.get('papel')
        if new_role not in ['membro', 'congregado', 'secretario']:
            return Response({"detail": "Papel inválido fornecido."}, status=status.HTTP_400_BAD_REQUEST)

        user_to_approve.aprovado = True
        user_to_approve.aprovado_por = request.user
        user_to_approve.data_aprovacao = timezone.now()
        user_to_approve.papel = new_role
        user_to_approve.save()
        
        return Response({"detail": f"Usuário {user_to_approve.nome_completo} aprovado como {user_to_approve.get_papel_display()}."}, status=status.HTTP_200_OK)

class AdminRejectUserView(APIView):
    """
    View de API para um secretário rejeitar (excluir) um cadastro pendente.
    """
    permission_classes = [IsAuthenticated, IsSecretario]

    def delete(self, request, pk, format=None):
        try:
            user_to_reject = User.objects.get(pk=pk, aprovado=False)
        except User.DoesNotExist:
            return Response({"detail": "Usuário pendente não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        user_to_reject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AdminUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View de API para um secretário:
    - LER (GET) os detalhes completos de um usuário.
    - ATUALIZAR (PUT/PATCH) os dados de um usuário.
    - EXCLUIR (DELETE) um usuário.
    """
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsSecretario]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return AdminUserUpdateSerializer
        return UserProfileSerializer