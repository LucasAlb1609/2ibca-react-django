from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .models import ConfiguracaoSite, Departamento, SecaoLideranca, DiaSemana, EventoEspecial, Devocional
from django.conf import settings
from .serializers import ConfiguracaoSiteSerializer, DevocionalSerializer

# --- VIEWS DA API (VERSÃO CORRETA) ---

class ConfiguracaoSiteAPIView(APIView):
    """
    API View para buscar a configuração (singleton) do site.
    """
    def get(self, request, format=None):
        configuracao = ConfiguracaoSite.objects.first()
        if configuracao:
            # Passando o 'request' no contexto do serializer
            serializer = ConfiguracaoSiteSerializer(configuracao, context={'request': request})
            return Response(serializer.data)
        return Response({})

class DevocionalRecenteAPIView(APIView):
    """
    API View para buscar a devocional mais recente.
    """
    def get(self, request, format=None):
        devocional = Devocional.objects.order_by('-data_publicacao').first()
        if devocional:
            # Passando o 'request' no contexto do serializer
            serializer = DevocionalSerializer(devocional, context={'request': request})
            return Response(serializer.data)
        return Response({})

# --- VIEWS ANTIGAS (PARA RENDERIZAÇÃO DE TEMPLATES) ---
# Mantidas aqui para referência, mas não são usadas pela API do React

def index(request):
    try:
        configuracao = ConfiguracaoSite.objects.first()
    except:
        class DefaultConfig:
            titulo_video = 'Última Transmissão ao Vivo'
            link_youtube = 'https://www.youtube.com/watch?v=uXMkc5owHzY'
            tipo_imagem = 'capa-maravilhas'
            def get_imagem_url(self):
                return f"{settings.STATIC_URL}fotos/{self.tipo_imagem}.jpeg"
        configuracao = DefaultConfig()

    devocional_recente = Devocional.objects.order_by('-data_publicacao').first()
    context = {
        'configuracao': configuracao,
        'devocional': devocional_recente,
    }
    return render(request, 'home/index.html', context)

def historia(request):
    return render(request, 'historia.html')

def lideranca(request):
    secoes = SecaoLideranca.objects.prefetch_related('pessoas').all()
    context = {
        'secoes': secoes
    }
    return render(request, 'lideranca.html', context)

def departamentos(request):
    todos_departamentos = Departamento.objects.all()
    departamentos_por_categoria = {}
    categorias_existentes = []
    
    for dept in todos_departamentos:
        categoria_chave = dept.categoria
        categoria_display = dept.get_categoria_display()
        
        if categoria_chave not in departamentos_por_categoria:
            departamentos_por_categoria[categoria_chave] = {"nome_display": categoria_display, "lista": []}
            if (categoria_chave, categoria_display) not in categorias_existentes:
                 categorias_existentes.append((categoria_chave, categoria_display))
        departamentos_por_categoria[categoria_chave]["lista"].append(dept)
        
    categorias_existentes.sort(key=lambda item: item[1])
    context = {
        "departamentos_agrupados": departamentos_por_categoria,
        "categorias_para_abas": categorias_existentes 
    }
    return render(request, "home/departamentos.html", context)

def congregacoes(request):
    return render(request, 'congregacoes.html')

def agenda(request):
    dias_semana = DiaSemana.objects.prefetch_related('eventos').all()
    eventos_especiais = EventoEspecial.objects.all()
    context = {
        'dias_semana': dias_semana,
        'eventos_especiais': eventos_especiais,
    }
    return render(request, 'agenda.html', context)

def lista_devocionais(request):
    devocionais = Devocional.objects.all()
    context = {
        'devocionais': devocionais
    }
    return render(request, 'home/lista_devocionais.html', context)
