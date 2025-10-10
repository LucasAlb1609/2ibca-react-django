import React, { useState, useEffect } from 'react';

// As imagens devem estar na sua pasta `public/fotos/`
const slides = [
  { image: '/fotos/tema-2025.jpg', alt: 'Tema 2025' },
  { image: '/fotos/equipe-2.jpg', alt: 'Equipe da Igreja 2' },
  { image: '/fotos/equipe-1.jpg', alt: 'Equipe da Igreja 1' },
];

function Carrossel() {
  const [currentSlide, setCurrentSlide] = useState(0);

  // Efeito para avançar o slide a cada 4 segundos
  useEffect(() => {
    const slideInterval = setInterval(() => {
      setCurrentSlide((prev) => (prev === slides.length - 1 ? 0 : prev + 1));
    }, 4000);

    return () => clearInterval(slideInterval);
  }, []);

  return (
    <div className="relative w-full h-[60vh] md:h-[80vh] lg:h-screen overflow-hidden">
      {/* Imagens dos Slides */}
      {slides.map((slide, index) => (
        <div
          key={index}
          className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
            index === currentSlide ? 'opacity-100' : 'opacity-0'
          }`}
        >
          <img src={slide.image} alt={slide.alt} className="w-full h-full object-cover" />
        </div>
      ))}
      
      {/* Indicadores (bolinhas) */}
      <div className="absolute bottom-5 left-1/2 -translate-x-1/2 flex space-x-3">
        {slides.map((_, index) => (
          <button
            key={index}
            onClick={() => setCurrentSlide(index)}
            className={`w-4 h-4 rounded-full border-2 border-white transition-colors ${
              index === currentSlide ? 'bg-white' : 'bg-transparent hover:bg-white/50'
            }`}
            aria-label={`Ir para o slide ${index + 1}`}
          />
        ))}
      </div>
    </div>
  );
}

export default Carrossel;