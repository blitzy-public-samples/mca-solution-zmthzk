from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EmailMetadata(BaseModel):
    sender: str
    subject: str
    body: str
    received_at: datetime

class Attachment(BaseModel):
    type: str
    file_path: str
    uploaded_at: datetime

class Merchant(BaseModel):
    legal_name: str
    dba_name: str
    federal_tax_id: str
    address: str
    industry: str
    annual_revenue: float

class Owner(BaseModel):
    name: str
    ssn: str
    address: str
    date_of_birth: datetime
    ownership_percentage: float

class FundingDetails(BaseModel):
    amount_requested: float
    use_of_funds: str

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

# HUMAN ASSISTANCE NEEDED
# Consider adding validation rules for fields like SSN, federal_tax_id, and email format.
# Also, consider adding additional optional fields that might be useful for the application process.