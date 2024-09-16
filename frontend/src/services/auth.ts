import axios from 'axios';

const AUTH_BASE_URL = process.env.REACT_APP_AUTH_BASE_URL;

export const login = async (email: string, password: string): Promise<string> => {
  try {
    const loginUrl = `${AUTH_BASE_URL}/login`;
    const response = await axios.post(loginUrl, { email, password });
    return response.data.token;
  } catch (error) {
    throw new Error('Login failed');
  }
};

export const logout = async (): Promise<void> => {
  try {
    const logoutUrl = `${AUTH_BASE_URL}/logout`;
    await axios.post(logoutUrl);
    localStorage.removeItem('authToken');
    sessionStorage.removeItem('authToken');
  } catch (error) {
    console.error('Logout failed', error);
  }
};