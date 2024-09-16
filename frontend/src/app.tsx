import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Provider } from '@reduxjs/toolkit';
import { store } from './store';
import Dashboard from './components/Dashboard';
import ApplicationList from './components/ApplicationList';
import ApplicationDetails from './components/ApplicationDetails';
import WebhookManagement from './components/WebhookManagement';
import UserManagement from './components/UserManagement';
import Home from './pages/Home';
import Applications from './pages/Applications';
import Webhooks from './pages/Webhooks';
import Settings from './pages/Settings';

const App: React.FC = () => {
  return (
    <Provider store={store}>
      <BrowserRouter>
        <div className="app-container">
          <nav>
            {/* HUMAN ASSISTANCE NEEDED: Add navigation menu items */}
          </nav>
          <main>
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/applications" element={<Applications />} />
              <Route path="/webhooks" element={<Webhooks />} />
              <Route path="/settings" element={<Settings />} />
            </Routes>
          </main>
        </div>
      </BrowserRouter>
    </Provider>
  );
};

export default App;