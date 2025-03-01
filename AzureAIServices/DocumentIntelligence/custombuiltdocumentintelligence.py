from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential
from AzureAIServices.DocumentIntelligence.prebuiltdocumentintelligence import document_analysis_client
import os

# Azure credentials
AZURE_FORM_RECOGNIZER_ENDPOINT = os.getenv("AZURE_FORM_RECOGNIZER_ENDPOINT") # "https://your-resource-name.cognitiveservices.azure.com/"
AZURE_FORM_RECOGNIZER_KEY = os.getenv("AZURE_FORM_RECOGNIZER_KEY") # "your-api-key"

admin_client = DocumentModelAdministrationClient(
    endpoint=AZURE_FORM_RECOGNIZER_ENDPOINT,
    credential=AzureKeyCredential(AZURE_FORM_RECOGNIZER_KEY)
)

# Azure blob storage
poller = admin_client.begin_build_model(
    source="https://your-storage-account.blob.core.windows.net/container-name",
    build_mode="template"
)

custom_model = poller.result()
print(f"Custom Model ID: {custom_model.model_id}")

with open("custom-document.jpg", "rb") as document_file:
    poller = document_analysis_client.begin_analyze_document(
        model_id="your-custom-model-id",
        document=document_file
    )
    result = poller.result()

for field_name, field_value in result.documents[0].fields.items():
    if field_value.confidence > 0.7:
        print(f"{field_name}: {field_value.value} (Confidence: {field_value.confidence})")
