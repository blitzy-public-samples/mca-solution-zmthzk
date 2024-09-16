import axios from 'axios';

const WEBHOOK_BASE_URL = process.env.REACT_APP_WEBHOOK_BASE_URL;

interface Webhook {
  id: string;
  url: string;
  events: string[];
}

interface WebhookRegistration {
  url: string;
  events: string[];
}

export const fetchWebhooks = async (): Promise<Webhook[]> => {
  const endpoint = `${WEBHOOK_BASE_URL}/webhooks`;
  const response = await axios.get(endpoint);
  return response.data as Webhook[];
};

// HUMAN ASSISTANCE NEEDED
// This function has a confidence level below 0.8 and may need review
export const registerWebhook = async (webhookData: WebhookRegistration): Promise<Webhook> => {
  const endpoint = `${WEBHOOK_BASE_URL}/webhooks`;
  const response = await axios.post(endpoint, webhookData);
  return response.data as Webhook;
};

export const deleteWebhook = async (webhookId: string): Promise<void> => {
  const endpoint = `${WEBHOOK_BASE_URL}/webhooks/${webhookId}`;
  await axios.delete(endpoint);
};