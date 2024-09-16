import React from 'react';
import { useQuery } from 'react-query';
import { fetchApplications } from '../services/api';
import { Application } from '../schema/applicationSchema';

const ApplicationList: React.FC = () => {
  const { data, isLoading, error } = useQuery<Application[], Error>('applications', fetchApplications);

  if (isLoading) {
    return <div>Loading applications...</div>;
  }

  if (error) {
    return <div>Error fetching applications: {error.message}</div>;
  }

  return (
    <div>
      <h2>MCA Applications</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Applicant Name</th>
            <th>Status</th>
            <th>Submission Date</th>
          </tr>
        </thead>
        <tbody>
          {data?.map((application) => (
            <tr key={application.id}>
              <td>{application.id}</td>
              <td>{application.applicantName}</td>
              <td>{application.status}</td>
              <td>{new Date(application.submissionDate).toLocaleDateString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
      {/* HUMAN ASSISTANCE NEEDED */}
      {/* Implement pagination or infinite scrolling here */}
      {/* This part requires more context about the desired UX and available backend API endpoints */}
    </div>
  );
};

export default ApplicationList;