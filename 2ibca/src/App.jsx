import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './pages/HomePage';
import HistoriaPage from './pages/HistoriaPage';
import LiderancaPage from './pages/LiderancaPage';
import DepartamentosPage from './pages/DepartamentosPage';
import AgendaPage from './pages/AgendaPage';

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/historia" element={<HistoriaPage />} />
          <Route path="/lideranca" element={<LiderancaPage />} />
          <Route path="/departamentos" element={<DepartamentosPage/>} />
          <Route path="/agenda" element={<AgendaPage/>} />
          {/* Outras rotas virão aqui no futuro */}
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export default App;