import unittest
from unittest.mock import patch, MagicMock
from services.ocr_service import OCRService
from models.iso_application import ISOApplication
from models.merchant import Merchant
from models.funding_details import FundingDetails
from models.owner import Owner

class TestOCRService(unittest.TestCase):

    def setUp(self):
        self.ocr_service = OCRService()

    @patch('services.ocr_service.pytesseract')
    def test_extract_data_from_iso_application(self, mock_pytesseract):
        mock_pytesseract.image_to_string.return_value = "Merchant Name: Test Merchant\nFunding Amount: $10000\nOwner: John Doe"
        
        result = self.ocr_service.extract_data_from_iso_application("test_image.jpg")
        
        self.assertIsInstance(result, ISOApplication)
        self.assertEqual(result.merchant.name, "Test Merchant")
        self.assertEqual(result.funding_details.amount, 10000)
        self.assertEqual(result.owner.name, "John Doe")

    @patch('services.ocr_service.pytesseract')
    def test_handle_handwritten_scan(self, mock_pytesseract):
        mock_pytesseract.image_to_string.return_value = "Merchant Name: Hand Written Merchant\nFunding Amount: $5000\nOwner: Jane Smith"
        
        result = self.ocr_service.extract_data_from_iso_application("handwritten_image.jpg")
        
        self.assertIsInstance(result, ISOApplication)
        self.assertEqual(result.merchant.name, "Hand Written Merchant")
        self.assertEqual(result.funding_details.amount, 5000)
        self.assertEqual(result.owner.name, "Jane Smith")

    def test_extract_merchant_details(self):
        text = "Merchant Name: ABC Corp\nAddress: 123 Main St\nCity: New York\nState: NY\nZip: 10001"
        merchant = self.ocr_service.extract_merchant_details(text)
        
        self.assertIsInstance(merchant, Merchant)
        self.assertEqual(merchant.name, "ABC Corp")
        self.assertEqual(merchant.address, "123 Main St")
        self.assertEqual(merchant.city, "New York")
        self.assertEqual(merchant.state, "NY")
        self.assertEqual(merchant.zip_code, "10001")

    def test_extract_funding_details(self):
        text = "Funding Amount: $15000\nTerm: 12 months\nRate: 1.5%"
        funding = self.ocr_service.extract_funding_details(text)
        
        self.assertIsInstance(funding, FundingDetails)
        self.assertEqual(funding.amount, 15000)
        self.assertEqual(funding.term, 12)
        self.assertEqual(funding.rate, 1.5)

    def test_extract_owner_information(self):
        text = "Owner: Alice Johnson\nSSN: 123-45-6789\nDOB: 01/15/1980"
        owner = self.ocr_service.extract_owner_information(text)
        
        self.assertIsInstance(owner, Owner)
        self.assertEqual(owner.name, "Alice Johnson")
        self.assertEqual(owner.ssn, "123-45-6789")
        self.assertEqual(owner.dob, "01/15/1980")

    def test_error_handling_invalid_image(self):
        with self.assertRaises(ValueError):
            self.ocr_service.extract_data_from_iso_application("non_existent_image.jpg")

    def test_data_validation(self):
        text = "Merchant Name: Invalid Data Corp\nFunding Amount: Not a number\nOwner: 12345"
        
        with self.assertRaises(ValueError):
            self.ocr_service.extract_data_from_iso_application("invalid_data_image.jpg")

    # HUMAN ASSISTANCE NEEDED
    # The following test case might need adjustments based on the actual implementation of confidence scoring in the OCR service
    def test_low_confidence_extraction(self):
        with patch.object(self.ocr_service, 'get_extraction_confidence', return_value=0.6):
            result = self.ocr_service.extract_data_from_iso_application("low_quality_image.jpg")
            self.assertIsNone(result)
            # Add appropriate assertions based on how low confidence results are handled in the actual implementation

if __name__ == '__main__':
    unittest.main()