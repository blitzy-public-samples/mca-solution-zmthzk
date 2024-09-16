from google.cloud import vision
from backend.app.core.config import settings
from backend.app.schema.application_schema import Application

# HUMAN ASSISTANCE NEEDED
# The following code is a basic implementation and may need refinement for production use.
# Additional error handling, input validation, and optimization might be required.

def extract_application_data(file_path: str) -> dict:
    # Initialize Google Cloud Vision client
    client = vision.ImageAnnotatorClient()

    # Load the document from the file path
    with open(file_path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform OCR using Vision API
    response = client.document_text_detection(image=image)

    # Process the OCR results
    text = response.full_text_annotation.text

    # Extract relevant information (merchant details, funding details, owner information)
    # This is a placeholder implementation and needs to be refined based on the actual document structure
    extracted_data = {
        "merchant_name": "",
        "merchant_address": "",
        "funding_amount": "",
        "owner_name": "",
        "owner_address": "",
    }

    # Placeholder logic for extracting information
    lines = text.split('\n')
    for line in lines:
        if "Merchant Name:" in line:
            extracted_data["merchant_name"] = line.split("Merchant Name:")[1].strip()
        elif "Merchant Address:" in line:
            extracted_data["merchant_address"] = line.split("Merchant Address:")[1].strip()
        elif "Funding Amount:" in line:
            extracted_data["funding_amount"] = line.split("Funding Amount:")[1].strip()
        elif "Owner Name:" in line:
            extracted_data["owner_name"] = line.split("Owner Name:")[1].strip()
        elif "Owner Address:" in line:
            extracted_data["owner_address"] = line.split("Owner Address:")[1].strip()

    # Return the extracted data as a dictionary
    return extracted_data