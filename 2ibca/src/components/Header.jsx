// src/components/Header.jsx

import React from 'react';
// Importe o Link do React Router para navegação
import { Link } from 'react-router-dom';

function Header() {
  // Vamos usar /logo.png que deve estar na pasta `public` do seu projeto React
  const logoUrl = '/logo.png'; 

  return (
    <header className="bg-blue-600 text-white p-2 flex items-center justify-between sticky top-0 z-50 shadow-md">
      {/* Seção do Logo */}
      <div className="flex items-end">
        <Link to="/">
          <img src={logoUrl} alt="Logo 2IBCA" className="h-16 w-auto transition-transform duration-300 hover:scale-110" />
        </Link>
        <Link to="/" className="no-underline text-white ml-2 hidden md:block">
          <h5 className="text-sm font-bold font-sans leading-tight">
            SEGUNDA IGREJA<br />BATISTA EM CASA AMARELA
          </h5>
        </Link>
      </div>

      {/* Navegação - Por enquanto, vamos colocar placeholders */}
      <nav>
        {/* O menu de navegação completo com dropdowns virá aqui em uma próxima etapa */}
        <div className="hidden md:flex space-x-4 font-bold">
          <Link to="/" className="hover:bg-blue-500 px-3 py-2 rounded-md">Nossa Igreja</Link>
          <Link to="/" className="hover:bg-blue-500 px-3 py-2 rounded-md">Agenda</Link>
          <Link to="/" className="hover:bg-blue-500 px-3 py-2 rounded-md">Podcast</Link>
          <Link to="/" className="hover:bg-blue-500 px-3 py-2 rounded-md">Contato</Link>
        </div>
        {/* Botão de Menu Mobile (Lógica virá depois) */}
        <div className="md:hidden">
          <button className="text-white">
            {/* Ícone de Menu (SVG) */}
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16m-7 6h7" />
            </svg>
          </button>
        </div>
      </nav>
    </header>
  );
}

export default Header;