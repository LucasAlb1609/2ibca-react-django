from rest_framework import serializers
from .models import ConfiguracaoSite, Devocional # Já podemos importar os dois

class ConfiguracaoSiteSerializer(serializers.ModelSerializer):
    imagem_url = serializers.CharField(source='get_imagem_url', read_only=True)

    class Meta:
        model = ConfiguracaoSite
        fields = ['link_youtube', 'titulo_video', 'imagem_url']

# Também já vamos criar o serializer da Devocional para a próxima etapa
class DevocionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devocional
        # Inclua os campos que o frontend precisará
        fields = ['id', 'titulo', 'subtitulo', 'autor', 'imagem', 'conteudo', 'data_publicacao']