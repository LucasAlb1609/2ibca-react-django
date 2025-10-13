import React, { useState, useEffect } from 'react';
import API_URL from '../services/api';
import Slider from 'react-slick';
import useOnScreen from '../hooks/useOnScreen';

// --- Componente Modal ---
function PessoaModal({ pessoa, onClose }) {
  if (!pessoa) return null;

  return (
    // Overlay
    <div 
      className="fixed inset-0 bg-black/80 flex items-center justify-center z-50 p-4 transition-opacity duration-300"
      onClick={onClose}
    >
      {/* Conteúdo do Modal */}
      <div 
        className="bg-white rounded-lg shadow-xl w-full max-w-2xl flex flex-col md:flex-row overflow-hidden"
        onClick={e => e.stopPropagation()} // Impede que o clique dentro do modal o feche
      >
        <img src={pessoa.foto || '/fotos/default-user.png'} alt={pessoa.nome} className="w-full md:w-1/3 h-64 md:h-auto object-cover" />
        <div className="p-6 flex flex-col">
          <h3 className="text-blue-600 text-2xl font-bold">{pessoa.nome}</h3>
          <h4 className="text-[#d9971c] text-lg font-bold mb-4">{pessoa.cargo}</h4>
          <p className="text-gray-600 text-base leading-relaxed overflow-y-auto">
            {pessoa.descricao}
          </p>
          <button onClick={onClose} className="mt-auto ml-auto bg-gray-200 text-gray-800 px-4 py-2 rounded-md hover:bg-gray-300 transition-colors">
            Fechar
          </button>
        </div>
      </div>
    </div>
  );
}

// --- Componente Card (COM AS CORREÇÕES) ---
function PessoaCard({ pessoa, onClick }) {
  const fotoUrl = pessoa.foto || '/fotos/default-user.png';
  
  const truncate = (text, length) => text.length > length ? text.substring(0, length) + '...' : text;

  return (
    // 1. Garantimos que o card ocupe a altura total (h-full) e seja um container flex vertical
    <div 
      className="bg-white rounded-lg p-5 text-center shadow-md transition-all duration-300 ease-in-out hover:-translate-y-2 hover:shadow-xl group h-full flex flex-col cursor-pointer"
      onClick={onClick}
    >
      <div className="h-64 w-full mb-4 rounded-md overflow-hidden">
        <img src={fotoUrl} alt={pessoa.nome} className="w-full h-full object-cover object-top transition-transform duration-300 group-hover:scale-110" />
      </div>
      {/* 2. Este container flex-grow vai ocupar todo o espaço restante do card */}
      <div className="flex flex-col flex-grow">
        <h3 className="text-blue-600 text-xl font-bold mb-1">{pessoa.nome}</h3>
        <h4 className="text-[#d9971c] text-base font-bold mb-2">{pessoa.cargo}</h4>
        
        {/* --- ALTERAÇÃO AQUI --- */}
        {/* 3. Removemos 'mt-auto' e adicionamos 'mt-4' para um espaçamento consistente. */}
        {/* 'min-h-[3.75rem]' reserva espaço para ~3 linhas de texto 'text-sm', forçando o alinhamento. */}
        <p className="text-gray-500 text-sm leading-relaxed mt-4 min-h-[3.75rem]">
          {truncate(pessoa.descricao, 80)}
        </p>
      </div>
    </div>
  );
}

// --- Componente da Página ---
function LiderancaPage() {
  const [secoes, setSecoes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedPessoa, setSelectedPessoa] = useState(null);
  const [secaoRef, isSecaoVisible] = useOnScreen({ threshold: 0.1 });

  useEffect(() => {
    const fetchLideranca = async () => {
      try {
        const response = await fetch(`${API_URL}/lideranca/`);
        if (!response.ok) throw new Error('Não foi possível buscar os dados de liderança.');
        const data = await response.json();
        setSecoes(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    fetchLideranca();
  }, []);

  const carouselSettings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 4,
    slidesToScroll: 1,
    autoplay: isSecaoVisible,
    autoplaySpeed: 4000,
    pauseOnHover: true,
    responsive: [
      { breakpoint: 1024, settings: { slidesToShow: 3 } },
      { breakpoint: 768, settings: { slidesToShow: 2 } },
      { breakpoint: 640, settings: { slidesToShow: 1 } },
    ],
  };

  if (loading) return <div className="flex justify-center items-center h-screen font-semibold italic">Carregando Liderança...</div>;
  if (error) return <div className="flex justify-center items-center h-screen text-red-500 font-semibold italic">Erro: {error}</div>;

  return (
    <div className="font-sans not-italic">
      {secoes.map((secao) => (
        <section key={secao.id} ref={secaoRef} className="bg-blue-600 py-16 text-white text-center">
          <div className="container mx-auto px-4">
            <h2 className="text-4xl font-bold mb-4">{secao.titulo}</h2>
            {secao.descricao && <p className="max-w-3xl mx-auto mb-12 text-lg opacity-90">{secao.descricao}</p>}
            
            {/* Lógica Condicional: Grid ou Carrossel */}
            {secao.pessoas.length > 4 ? (
              <Slider {...carouselSettings}>
                {secao.pessoas.map((pessoa) => (
                  <div key={pessoa.id} className="px-4 h-full">
                    <PessoaCard pessoa={pessoa} onClick={() => setSelectedPessoa(pessoa)} />
                  </div>
                ))}
              </Slider>
            ) : (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 justify-center">
                {secao.pessoas.map((pessoa) => (
                  <PessoaCard key={pessoa.id} pessoa={pessoa} onClick={() => setSelectedPessoa(pessoa)} />
                ))}
              </div>
            )}
          </div>
        </section>
      ))}

      {/* Renderização do Modal */}
      {selectedPessoa && <PessoaModal pessoa={selectedPessoa} onClose={() => setSelectedPessoa(null)} />}
    </div>
  );
}

export default LiderancaPage;