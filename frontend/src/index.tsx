import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import App from './app';
import rootReducer from './store';
import { setupAxiosInterceptors } from './services/api';

const store = configureStore({ reducer: rootReducer });

const setupApp = () => {
  setupAxiosInterceptors();

  ReactDOM.render(
    <React.StrictMode>
      <Provider store={store}>
        <App />
      </Provider>
    </React.StrictMode>,
    document.getElementById('root')
  );
};

setupApp();