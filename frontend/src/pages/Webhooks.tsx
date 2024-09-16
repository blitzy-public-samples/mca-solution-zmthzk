import React, { useState, useEffect } from 'react';
import WebhookManagement from '../components/WebhookManagement';
import { fetchWebhooks, registerWebhook, deleteWebhook } from '../services/webhook';

// HUMAN ASSISTANCE NEEDED
// The following component may need additional error handling, loading states, and potentially pagination for production readiness.
const Webhooks: React.FC = () => {
  const [webhooks, setWebhooks] = useState<any[]>([]);

  useEffect(() => {
    const loadWebhooks = async () => {
      try {
        const fetchedWebhooks = await fetchWebhooks();
        setWebhooks(fetchedWebhooks);
      } catch (error) {
        console.error('Failed to fetch webhooks:', error);
        // TODO: Implement proper error handling
      }
    };

    loadWebhooks();
  }, []);

  const handleAddWebhook = async (webhookData: any) => {
    try {
      const newWebhook = await registerWebhook(webhookData);
      setWebhooks([...webhooks, newWebhook]);
    } catch (error) {
      console.error('Failed to add webhook:', error);
      // TODO: Implement proper error handling
    }
  };

  const handleRemoveWebhook = async (webhookId: string) => {
    try {
      await deleteWebhook(webhookId);
      setWebhooks(webhooks.filter(webhook => webhook.id !== webhookId));
    } catch (error) {
      console.error('Failed to remove webhook:', error);
      // TODO: Implement proper error handling
    }
  };

  return (
    <div>
      <h1>Webhooks</h1>
      <WebhookManagement
        webhooks={webhooks}
        onAddWebhook={handleAddWebhook}
        onRemoveWebhook={handleRemoveWebhook}
      />
    </div>
  );
};

export default Webhooks;