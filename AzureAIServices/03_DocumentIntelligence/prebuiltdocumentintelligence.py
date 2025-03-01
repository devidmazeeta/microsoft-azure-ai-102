from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

# Azure credentials
AZURE_FORM_RECOGNIZER_ENDPOINT = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT") # https://your-resource-name.cognitiveservices.azure.com/
AZURE_FORM_RECOGNIZER_KEY = os.getenv("AZURE_FORM_RECOGNIZER_KEY") # your-api-key

document_analysis_client = DocumentAnalysisClient(
    endpoint=AZURE_FORM_RECOGNIZER_ENDPOINT,
    credential=AzureKeyCredential(AZURE_FORM_RECOGNIZER_KEY)
)

# Extract Text from a Document
document_path = "./Input/invoice.pdf"  # Path to your document

with open(document_path, "rb") as document_file:
    poller = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-invoice",  # Using the prebuilt invoice model
        document=document_file
    )
    result = poller.result()

# Display extracted information
for idx, field in enumerate(result.documents):
    print(f"Document {idx + 1}")
    for name, value in field.fields.items():
        print(f"{name}: {value.value} (Confidence: {value.confidence})")

# Extract Data from a Receipt
with open("./Input/receipt.jpg", "rb") as document_file:
    poller = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-receipt",
        document=document_file
    )
    result = poller.result()

# Display receipt details
for receipt in result.documents:
    print(f"Merchant: {receipt.fields.get('MerchantName').value}")
    print(f"Transaction Date: {receipt.fields.get('TransactionDate').value}")
    print(f"Total Amount: {receipt.fields.get('Total').value}")
