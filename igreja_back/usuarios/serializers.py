from rest_framework import serializers
from .models import User, Filho
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer de token personalizado para adicionar informações extras do usuário
    (como nome_completo e papel) ao payload do token de acesso.
    """
    @classmethod
    def get_token(cls, user):
        # Pega o token padrão
        token = super().get_token(user)

        # Adiciona nossos campos customizados ao payload do token
        token['username'] = user.username
        token['nome_completo'] = user.nome_completo
        token['papel'] = user.papel
        
        return token

class FilhoSerializer(serializers.ModelSerializer):
    """ Serializer para os dados de um filho. """
    class Meta:
        model = Filho
        # O campo 'user' será preenchido automaticamente na view
        fields = ['nome_completo', 'data_nascimento']

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer para o processo de cadastro de um novo usuário.
    Lida com a validação de senha e a criação aninhada de filhos.
    """
    # Campo extra para confirmação de senha, não será salvo no banco
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    # Campo para receber uma lista de filhos, também não é um campo direto do modelo User
    filhos = FilhoSerializer(many=True, required=False, write_only=True)

    class Meta:
        model = User
        # Lista de todos os campos que o frontend enviará no cadastro
        fields = (
            'username', 'email', 'password', 'password2', 'nome_completo', 'foto_perfil',
            'data_nascimento', 'nome_pai', 'nome_mae', 'cpf', 'rg', 'naturalidade',
            'estado_civil', 'nome_conjuge', 'data_casamento', 'telefone', 'endereco',
            'bairro', 'cidade', 'cep', 'profissao', 'nivel_escolar', 'data_conversao',
            'batizado_aguas', 'data_batismo', 'local_batismo', 'outra_igreja_batismo',
            'recebido_por_aclamacao', 'membro_congregacao', 'qual_congregacao',
            'frequenta_escola_biblica', 'qual_classe_escola_biblica',
            'deseja_exercer_funcao', 'qual_funcao_deseja', 'tem_alergia_medicacao',
            'alergias_texto', 'filhos'
        )
        extra_kwargs = {
            'password': {'write_only': True} # Garante que a senha não seja retornada na resposta
        }

    def validate(self, data):
        """
        Validação customizada para verificar se as senhas coincidem.
        """
        if data['password'] != data.get('password2'):
            raise serializers.ValidationError({"password": "As senhas não coincidem."})
        # A validação do CPF duplicado já é feita pelo 'unique=True' no models.py
        return data

    def create(self, validated_data):
        """
        Cria o objeto User e os objetos Filho associados.
        """
        # Remove os dados que não fazem parte do modelo User antes de criá-lo
        filhos_data = validated_data.pop('filhos', [])
        validated_data.pop('password2', None)
        
        # Usa create_user para garantir que a senha seja criptografada (hashed)
        user = User.objects.create_user(**validated_data)
        
        # Cria os filhos associados ao usuário recém-criado
        for filho_data in filhos_data:
            Filho.objects.create(user=user, **filho_data)
            
        return user