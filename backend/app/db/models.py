from google.cloud.firestore import Client
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from backend.app.schema.application_schema import EmailMetadata, Attachment, Merchant, Owner, FundingDetails

class Application(BaseModel):
    id: str
    status: str
    created_at: datetime
    updated_at: datetime
    email_metadata: EmailMetadata
    attachments: List[Attachment]
    merchant: Merchant
    owners: List[Owner]
    funding_details: FundingDetails

class Webhook(BaseModel):
    id: str
    url: str
    secret: str
    active: bool