import React, { useState } from 'react';
import { UserManagement } from '../components/UserManagement';
import { updateUserSettings } from '../services/auth';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional refinement and error handling for production readiness.
// Please review and enhance as necessary.

const Settings: React.FC = () => {
  const [settings, setSettings] = useState({
    email: '',
    notifications: false,
    theme: 'light',
  });

  const [isAdmin, setIsAdmin] = useState(false); // This should be determined from user role

  const handleSettingsUpdate = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    try {
      await updateUserSettings(settings);
      // Add success message or notification here
    } catch (error) {
      // Add error handling here
      console.error('Failed to update settings:', error);
    }
  };

  return (
    <div className="settings-page">
      <h1>User Settings</h1>
      <form onSubmit={handleSettingsUpdate}>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={settings.email}
            onChange={(e) => setSettings({ ...settings, email: e.target.value })}
          />
        </div>
        <div>
          <label htmlFor="notifications">
            <input
              type="checkbox"
              id="notifications"
              checked={settings.notifications}
              onChange={(e) => setSettings({ ...settings, notifications: e.target.checked })}
            />
            Receive notifications
          </label>
        </div>
        <div>
          <label htmlFor="theme">Theme:</label>
          <select
            id="theme"
            value={settings.theme}
            onChange={(e) => setSettings({ ...settings, theme: e.target.value })}
          >
            <option value="light">Light</option>
            <option value="dark">Dark</option>
          </select>
        </div>
        <button type="submit">Save Settings</button>
      </form>

      {isAdmin && <UserManagement />}
    </div>
  );
};

export default Settings;