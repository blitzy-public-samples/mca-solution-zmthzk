import axios from 'axios';
import { Application } from '../schema/applicationSchema';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const fetchApplications = async (page: number, limit: number): Promise<Application[]> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/applications`, {
      params: { page, limit }
    });
    return response.data as Application[];
  } catch (error) {
    console.error('Error fetching applications:', error);
    throw error;
  }
};

export const fetchApplicationDetails = async (applicationId: string): Promise<Application> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/applications/${applicationId}`);
    return response.data as Application;
  } catch (error) {
    console.error('Error fetching application details:', error);
    throw error;
  }
};

// HUMAN ASSISTANCE NEEDED
// This function has a lower confidence level and may need review for production readiness
export const updateApplication = async (applicationId: string, updatedData: Partial<Application>): Promise<Application> => {
  try {
    const response = await axios.put(`${API_BASE_URL}/applications/${applicationId}`, updatedData);
    return response.data as Application;
  } catch (error) {
    console.error('Error updating application:', error);
    throw error;
  }
};