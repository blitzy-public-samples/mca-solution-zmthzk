import React from 'react';
import { useQuery } from 'react-query';
import { fetchApplicationDetails } from '../services/api';
import { Application } from '../schema/applicationSchema';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional error handling, accessibility improvements, and styling adjustments for production readiness.

const ApplicationDetails: React.FC<{ applicationId: string }> = ({ applicationId }) => {
  const { data: application, isLoading, error } = useQuery<Application, Error>(
    ['application', applicationId],
    () => fetchApplicationDetails(applicationId)
  );

  if (isLoading) {
    return <div>Loading application details...</div>;
  }

  if (error) {
    return <div>Error loading application details: {error.message}</div>;
  }

  if (!application) {
    return <div>No application data found</div>;
  }

  return (
    <div className="application-details">
      <h2>Application Details</h2>
      
      <section>
        <h3>Merchant Information</h3>
        <p>Business Name: {application.businessName}</p>
        <p>DBA: {application.dba}</p>
        <p>Business Type: {application.businessType}</p>
        <p>Tax ID: {application.taxId}</p>
      </section>

      <section>
        <h3>Funding Details</h3>
        <p>Requested Amount: ${application.requestedAmount}</p>
        <p>Use of Funds: {application.useOfFunds}</p>
      </section>

      <section>
        <h3>Owner Information</h3>
        {application.owners.map((owner, index) => (
          <div key={index}>
            <p>Name: {owner.name}</p>
            <p>Ownership Percentage: {owner.ownershipPercentage}%</p>
          </div>
        ))}
      </section>

      <section>
        <h3>Attachments</h3>
        <ul>
          {application.attachments.map((attachment, index) => (
            <li key={index}>
              <a href={attachment.url} download>{attachment.name}</a>
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
};

export default ApplicationDetails;