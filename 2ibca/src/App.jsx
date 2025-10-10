import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow">
        {/* O sistema de rotas gerenciará qual página é exibida aqui */}
        <Routes>
          <Route path="/" element={<HomePage />} />
          {/* Outras rotas (como /noticias, /agenda) virão aqui no futuro */}
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export default App;