from azure.ai.formrecognizer import DocumentModelAdministrationClient

admin_client = DocumentModelAdministrationClient(
    endpoint=AZURE_FORM_RECOGNIZER_ENDPOINT,
    credential=AzureKeyCredential(AZURE_FORM_RECOGNIZER_KEY)
)

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
    print(f"{field_name}: {field_value.value} (Confidence: {field_value.confidence})")
