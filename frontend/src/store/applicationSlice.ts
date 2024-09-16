import { createSlice, PayloadAction, createAsyncThunk } from '@reduxjs/toolkit';
import { Application } from '../schema/applicationSchema';
import { fetchApplications as fetchApplicationsApi } from '../services/api';

export const fetchApplications = createAsyncThunk<Application[]>(
  'application/fetchApplications',
  async (_, { rejectWithValue }) => {
    try {
      const applications = await fetchApplicationsApi();
      return applications;
    } catch (error) {
      return rejectWithValue('Failed to fetch applications');
    }
  }
);

const applicationSlice = createSlice({
  name: 'application',
  initialState: {
    applications: [] as Application[],
    status: 'idle',
    error: null as string | null,
  },
  reducers: {
    setApplications: (state, action: PayloadAction<Application[]>) => {
      state.applications = action.payload;
    },
    updateApplication: (state, action: PayloadAction<Application>) => {
      const index = state.applications.findIndex(app => app.id === action.payload.id);
      if (index !== -1) {
        state.applications[index] = action.payload;
      }
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchApplications.pending, (state) => {
        state.status = 'loading';
        state.error = null;
      })
      .addCase(fetchApplications.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.applications = action.payload;
      })
      .addCase(fetchApplications.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.payload as string;
      });
  },
});

export const { setApplications, updateApplication } = applicationSlice.actions;
export default applicationSlice.reducer;

// HUMAN ASSISTANCE NEEDED
// The following areas may need review:
// 1. Error handling in the fetchApplications thunk could be more specific.
// 2. The updateApplication reducer assumes the application ID exists. Consider adding error handling.
// 3. Additional actions like addApplication or removeApplication might be useful.
// 4. Consider adding selectors for easier state access in components.