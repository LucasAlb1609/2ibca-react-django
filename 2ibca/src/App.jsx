import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import ScrollToTop from './components/ScrollToTop';
import RotaProtegida from './components/RotaProtegida';

import HomePage from './pages/HomePage';
import HistoriaPage from './pages/HistoriaPage';
import LiderancaPage from './pages/LiderancaPage';
import DepartamentosPage from './pages/DepartamentosPage';
import AgendaPage from './pages/AgendaPage';
import RegistroPage from './pages/RegistroPage'; 
import RegistroSucessoPage from './pages/RegistroSucessoPage'; 
import PaginaLogin from './pages/PaginaLogin';
import PaginaDashboard from './pages/PaginaDashboard';
import PaginaPerfil from './pages/PaginaPerfil';
import PaginaEditarPerfil from './pages/PaginaEditarPerfil';
import PaginaListaUsuarios from './pages/PaginaListaUsuarios';
import PaginaUsuariosPendentes from './pages/PaginaUsuariosPendentes';
import PaginaCriarUsuario from './pages/PaginaCriarUsuario';

function App() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />
      <ScrollToTop />
      <main className="flex-grow">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/historia" element={<HistoriaPage />} />
          <Route path="/lideranca" element={<LiderancaPage />} />
          <Route path="/departamentos" element={<DepartamentosPage/>} />
          <Route path="/agenda" element={<AgendaPage/>} />
          <Route path="/cadastro" element={<RegistroPage />} />
          <Route path="/cadastro-sucesso" element={<RegistroSucessoPage />} />
          <Route path="/login" element={<PaginaLogin />} />
          {/* Outras rotas virão aqui no futuro */}

          {/* Rotas que requerem autenticação */}
          <Route path="/dashboard" element={<RotaProtegida><PaginaDashboard /></RotaProtegida>} />
          <Route path="/perfil" element={<RotaProtegida><PaginaPerfil /></RotaProtegida>} />
          <Route path="/perfil/editar" element={<RotaProtegida><PaginaEditarPerfil /></RotaProtegida>} />
          <Route path="/admin/todos-usuarios" element={<RotaProtegida><PaginaListaUsuarios /></RotaProtegida>} />
          <Route path="/admin/todos-usuarios" element={<RotaProtegida><PaginaListaUsuarios /></RotaProtegida>} />
          <Route path="/admin/usuarios-pendentes" element={<RotaProtegida><PaginaUsuariosPendentes /></RotaProtegida>} />
          <Route path="/admin/criar-usuario" element={<RotaProtegida><PaginaCriarUsuario /></RotaProtegida>} />

        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export default App;