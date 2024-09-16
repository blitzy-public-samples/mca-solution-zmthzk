import React, { useState, useEffect } from 'react';
import { ApplicationList } from '../components/ApplicationList';
import { fetchApplications } from '../services/api';

const Applications: React.FC = () => {
  const [applications, setApplications] = useState([]);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const loadApplications = async () => {
      setLoading(true);
      try {
        const data = await fetchApplications(page);
        setApplications(prevApplications => [...prevApplications, ...data]);
      } catch (error) {
        console.error('Error fetching applications:', error);
      } finally {
        setLoading(false);
      }
    };

    loadApplications();
  }, [page]);

  const handleLoadMore = () => {
    setPage(prevPage => prevPage + 1);
  };

  return (
    <div className="applications-page">
      <h1>MCA Applications</h1>
      <ApplicationList applications={applications} />
      {loading && <p>Loading...</p>}
      <button onClick={handleLoadMore} disabled={loading}>
        Load More
      </button>
    </div>
  );
};

export default Applications;

// HUMAN ASSISTANCE NEEDED
// The following aspects may need further consideration:
// 1. Error handling: Implement a more user-friendly way to display errors.
// 2. Empty state: Add a message or component to display when there are no applications.
// 3. Pagination: Implement proper pagination logic, including checking if there are more items to load.
// 4. Accessibility: Ensure the component and its children are fully accessible.
// 5. Performance optimization: Consider implementing virtualization for large lists.