// src/components/Footer.jsx

import React from 'react';

function Footer() {
  return (
    <footer className="bg-white text-gray-800 py-8">
      <div className="container mx-auto px-4">
        <div className="flex flex-wrap justify-between text-sm">
          {/* Coluna da Esquerda (Versículo) */}
          <div className="w-full md:w-2/5 mb-6 md:mb-0">
            <h3 className="font-bold text-lg mb-2">Gálatas 6. 2-10</h3>
            <p className="text-xs text-gray-600 leading-relaxed">
              ² Levai as cargas uns dos outros, e assim cumprireis a lei de Cristo...
              {/* (Restante do texto) */}
            </p>
          </div>

          {/* Coluna do Meio (Contato) */}
          <div className="w-full md:w-1/4 mb-6 md:mb-0">
            <h4 className="font-bold text-base mb-2">Contato</h4>
            <ul>
              <li className="mb-2">Rua Santa Izabel, 425 - Casa Amarela, Recife - PE</li>
              <li className="mb-2">contato@segundaigreja.org.br</li>
            </ul>
          </div>
          
          {/* Coluna da Direita (Outros) */}
          <div className="w-full md:w-1/4 mb-6 md:mb-0">
            <h4 className="font-bold text-base mb-2">Outros</h4>
            <ul>
              <li><a href="/admin" target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">Painel de Administrador</a></li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
  );
}

export default Footer;