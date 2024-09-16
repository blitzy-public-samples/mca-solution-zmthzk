import React from 'react';
import { useQuery } from 'react-query';
import { fetchDashboardData } from '../services/api';

const Dashboard: React.FC = () => {
  const { data, isLoading, error } = useQuery('dashboardData', fetchDashboardData);

  if (isLoading) {
    return <div>Loading dashboard data...</div>;
  }

  if (error) {
    return <div>Error fetching dashboard data. Please try again later.</div>;
  }

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      
      <section className="statistics">
        <h2>Application Statistics</h2>
        <div className="stat-grid">
          <div className="stat-item">
            <h3>Total Applications</h3>
            <p>{data.totalApplications}</p>
          </div>
          <div className="stat-item">
            <h3>Pending Review</h3>
            <p>{data.pendingReview}</p>
          </div>
          <div className="stat-item">
            <h3>Approved</h3>
            <p>{data.approved}</p>
          </div>
          <div className="stat-item">
            <h3>Rejected</h3>
            <p>{data.rejected}</p>
          </div>
        </div>
      </section>

      <section className="recent-activity">
        <h2>Recent Activity</h2>
        <ul>
          {data.recentActivity.map((activity, index) => (
            <li key={index}>
              <span>{activity.timestamp}</span>
              <span>{activity.action}</span>
              <span>{activity.applicationId}</span>
            </li>
          ))}
        </ul>
      </section>

      <section className="quick-actions">
        <h2>Quick Actions</h2>
        <div className="button-group">
          <button>New Application</button>
          <button>Review Pending</button>
          <button>Generate Report</button>
        </div>
      </section>
    </div>
  );
};

export default Dashboard;