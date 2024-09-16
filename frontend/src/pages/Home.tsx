import React from 'react';
import { Link } from 'react-router-dom';
import Dashboard from '../components/Dashboard';

const Home: React.FC = () => {
  return (
    <div className="home-container">
      <h1>Welcome to the MCA Application Processing System</h1>
      
      <div className="quick-links">
        <h2>Quick Links</h2>
        <ul>
          <li><Link to="/applications">View Applications</Link></li>
          <li><Link to="/new-application">Submit New Application</Link></li>
          <li><Link to="/reports">Reports</Link></li>
        </ul>
      </div>
      
      <Dashboard />
    </div>
  );
};

export default Home;