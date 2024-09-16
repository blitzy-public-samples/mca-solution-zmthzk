from requests import post
from backend.app.db.models import Webhook
from backend.app.core.config import settings

# HUMAN ASSISTANCE NEEDED
# The following function has a confidence level below 0.8 and may need review
def trigger_webhook(webhook_id: str, application_data: dict) -> bool:
    try:
        # Retrieve webhook configuration from database
        webhook = Webhook.get(webhook_id)
        if not webhook:
            return False

        # Prepare payload with application data
        payload = {
            "application_data": application_data,
            "webhook_id": webhook_id,
            "timestamp": str(datetime.utcnow())
        }

        # Send POST request to webhook URL
        response = post(
            webhook.url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=settings.WEBHOOK_TIMEOUT
        )

        # Handle response and potential errors
        response.raise_for_status()
        return True

    except Exception as e:
        # Log the error (implement proper logging)
        print(f"Error triggering webhook: {str(e)}")
        return False

def register_webhook(webhook_data: dict) -> str:
    # Validate webhook data
    if not all(key in webhook_data for key in ["url", "event_type"]):
        raise ValueError("Invalid webhook data. 'url' and 'event_type' are required.")

    # Create new Webhook record in database
    webhook = Webhook(
        url=webhook_data["url"],
        event_type=webhook_data["event_type"],
        description=webhook_data.get("description", ""),
        is_active=webhook_data.get("is_active", True)
    )
    webhook.save()

    # Return the ID of the created webhook
    return str(webhook.id)