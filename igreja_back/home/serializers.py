from rest_framework import serializers
from .models import ConfiguracaoSite, Devocional, SecaoLideranca, Pessoa

class ConfiguracaoSiteSerializer(serializers.ModelSerializer):
    imagem_url = serializers.SerializerMethodField()

    class Meta:
        model = ConfiguracaoSite
        fields = ['link_youtube', 'titulo_video', 'imagem_url']

    def get_imagem_url(self, obj):
        request = self.context.get('request')
        # O método obj.get_imagem_url() vem do seu models.py
        caminho_da_imagem = obj.get_imagem_url() 
        
        if caminho_da_imagem and request:
            # Esta linha adiciona "http://127.0.0.1:8000" ao caminho, seja ele /static/... ou /media/...
            return request.build_absolute_uri(caminho_da_imagem)
        return None

class DevocionalSerializer(serializers.ModelSerializer):
    imagem = serializers.SerializerMethodField()

    class Meta:
        model = Devocional
        fields = ['id', 'titulo', 'subtitulo', 'autor', 'imagem', 'conteudo', 'data_publicacao']

    def get_imagem(self, obj):
        request = self.context.get('request')
        if obj.imagem and request:
            return request.build_absolute_uri(obj.imagem.url)
        return None
    

class PessoaSerializer(serializers.ModelSerializer):
    # Serializer para o modelo 'Pessoa'
    foto = serializers.SerializerMethodField()

    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'cargo', 'descricao', 'foto']
    
    def get_foto(self, obj):
        request = self.context.get('request')
        if obj.foto and request:
            return request.build_absolute_uri(obj.foto.url)
        return None

class SecaoLiderancaSerializer(serializers.ModelSerializer):
    # Serializer para o modelo 'SecaoLideranca'
    # 2. Aninhamos o PessoaSerializer aqui
    # 'pessoas' é o related_name que definimos no models.py
    pessoas = PessoaSerializer(many=True, read_only=True)

    class Meta:
        model = SecaoLideranca
        fields = ['id', 'titulo', 'descricao', 'pessoas']