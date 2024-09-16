from google.cloud.firestore import Client
from backend.app.core.config import settings

db = Client(project=settings.GOOGLE_CLOUD_PROJECT)

def get_application(application_id: str) -> dict:
    doc_ref = db.collection('applications').document(application_id)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

def create_application(application_data: dict) -> str:
    doc_ref = db.collection('applications').document()
    doc_ref.set(application_data)
    return doc_ref.id

def update_application(application_id: str, update_data: dict) -> bool:
    doc_ref = db.collection('applications').document(application_id)
    doc_ref.update(update_data)
    return True

def delete_application(application_id: str) -> bool:
    doc_ref = db.collection('applications').document(application_id)
    doc_ref.delete()
    return True

def get_webhook(webhook_id: str) -> dict:
    doc_ref = db.collection('webhooks').document(webhook_id)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

def create_webhook(webhook_data: dict) -> str:
    doc_ref = db.collection('webhooks').document()
    doc_ref.set(webhook_data)
    return doc_ref.id

def update_webhook(webhook_id: str, update_data: dict) -> bool:
    doc_ref = db.collection('webhooks').document(webhook_id)
    doc_ref.update(update_data)
    return True

def delete_webhook(webhook_id: str) -> bool:
    doc_ref = db.collection('webhooks').document(webhook_id)
    doc_ref.delete()
    return True