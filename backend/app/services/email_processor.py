from google.cloud import storage
from email import message_from_bytes
from backend.app.core.config import settings
from backend.app.db.models import Application
from backend.app.schema.application_schema import EmailMetadata

# HUMAN ASSISTANCE NEEDED
# The following function needs review and potential modifications for production readiness.
# Specific areas that may need attention:
# - Error handling and logging
# - Proper authentication for Google Cloud Storage
# - Sanitization of email data
# - Handling of different email formats and encodings
# - Optimization for large attachments or high volume of emails

def process_email(email_data: bytes) -> str:
    # Parse the email data
    email_message = message_from_bytes(email_data)

    # Extract email metadata
    sender = email_message['From']
    subject = email_message['Subject']
    body = ""

    # Extract body based on content type
    if email_message.is_multipart():
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
                break
    else:
        body = email_message.get_payload(decode=True).decode()

    # Save attachments to Google Cloud Storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(settings.GCS_BUCKET_NAME)
    attachment_urls = []

    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename:
            blob = bucket.blob(f"attachments/{filename}")
            blob.upload_from_string(
                part.get_payload(decode=True),
                content_type=part.get_content_type()
            )
            attachment_urls.append(blob.public_url)

    # Create an Application record with email metadata
    email_metadata = EmailMetadata(
        sender=sender,
        subject=subject,
        body=body,
        attachment_urls=attachment_urls
    )

    application = Application(email_metadata=email_metadata)
    application.save()

    # Return the created application ID
    return str(application.id)