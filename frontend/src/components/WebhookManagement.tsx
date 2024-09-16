import React, { useState } from 'react';
import { useQuery, useMutation } from 'react-query';
import { fetchWebhooks, registerWebhook, deleteWebhook } from '../services/webhook';

// HUMAN ASSISTANCE NEEDED
// This component may need additional styling and error handling for production readiness.
// Consider adding form validation, loading states, and error messages.

const WebhookManagement: React.FC = () => {
  const [newWebhookUrl, setNewWebhookUrl] = useState('');

  const { data: webhooks, isLoading, isError, refetch } = useQuery('webhooks', fetchWebhooks);

  const registerMutation = useMutation(registerWebhook, {
    onSuccess: () => {
      refetch();
      setNewWebhookUrl('');
    },
  });

  const deleteMutation = useMutation(deleteWebhook, {
    onSuccess: () => refetch(),
  });

  const handleAddWebhook = (e: React.FormEvent) => {
    e.preventDefault();
    registerMutation.mutate(newWebhookUrl);
  };

  const handleDeleteWebhook = (webhookId: string) => {
    deleteMutation.mutate(webhookId);
  };

  const handleTestWebhook = (webhookUrl: string) => {
    // HUMAN ASSISTANCE NEEDED
    // Implement webhook testing functionality
    console.log('Testing webhook:', webhookUrl);
  };

  if (isLoading) return <div>Loading...</div>;
  if (isError) return <div>Error loading webhooks</div>;

  return (
    <div>
      <h2>Webhook Management</h2>
      
      <form onSubmit={handleAddWebhook}>
        <input
          type="url"
          value={newWebhookUrl}
          onChange={(e) => setNewWebhookUrl(e.target.value)}
          placeholder="Enter webhook URL"
          required
        />
        <button type="submit">Add Webhook</button>
      </form>

      <h3>Registered Webhooks</h3>
      <ul>
        {webhooks?.map((webhook) => (
          <li key={webhook.id}>
            {webhook.url}
            <button onClick={() => handleDeleteWebhook(webhook.id)}>Delete</button>
            <button onClick={() => handleTestWebhook(webhook.url)}>Test</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default WebhookManagement;