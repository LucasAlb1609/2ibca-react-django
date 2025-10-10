import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import HistoriaPage from './pages/HistoriaPage';

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/historia" element={<HistoriaPage />} /> {/* 2. Adicione a nova rota */}
          {/* Outras rotas virão aqui no futuro */}
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export default App;