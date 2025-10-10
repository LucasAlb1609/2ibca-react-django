import React, { useState, useEffect } from 'react';
import API_URL from '../services/api';

function HomePage() {
  // Estados para armazenar os dados da API
  const [configuracao, setConfiguracao] = useState(null);
  const [devocional, setDevocional] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Função para buscar todos os dados da página inicial
    const fetchData = async () => {
      try {
        // Promise.all executa as duas buscas em paralelo
        const [configResponse, devocionalResponse] = await Promise.all([
          fetch(`${API_URL}/configuracao/`),
          fetch(`${API_URL}/devocionais/recente/`)
        ]);

        if (!configResponse.ok || !devocionalResponse.ok) {
          throw new Error('Erro ao buscar dados da API');
        }

        const configData = await configResponse.json();
        const devocionalData = await devocionalResponse.json();

        setConfiguracao(configData);
        setDevocional(devocionalData);

        // Vamos exibir os dados no console do navegador para confirmar
        console.log("Dados da Configuração:", configData);
        console.log("Dados da Devocional:", devocionalData);

      } catch (err) {
        setError(err.message);
        console.error("Erro na busca de dados:", err);

      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []); // Array vazio garante que a busca só ocorra uma vez

  // Renderização condicional enquanto os dados são carregados ou em caso de erro
  if (loading) {
    return <p className="text-center p-10">Carregando...</p>;
  }

  if (error) {
    return <p className="text-center p-10 text-red-500">Erro: {error}</p>;
  }

  // Renderização principal quando os dados estiverem prontos
  return (
    <div>
      <h1 className="text-3xl font-bold text-center my-4">Página Inicial (React)</h1>
      {configuracao && (
        <div className="p-4 m-4 border rounded shadow">
          <h2 className="text-xl font-semibold">Seção de Vídeo</h2>
          <p>Título: {configuracao.titulo_video}</p>
          <a href={configuracao.link_youtube} target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">
            Assistir no YouTube
          </a>
        </div>
      )}
      {devocional && (
        <div className="p-4 m-4 border rounded shadow">
          <h2 className="text-xl font-semibold">Devocional da Semana</h2>
          <p>Título: {devocional.titulo}</p>
          <p>Autor: {devocional.autor}</p>
        </div>
      )}
    </div>
  );
}

export default HomePage;