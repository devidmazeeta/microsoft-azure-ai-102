from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace with your Azure resource credentials
endpoint = "https://<your-resource-name>.cognitiveservices.azure.com/"
api_key = "<your-api-key>"

# Initialize the client
credential = AzureKeyCredential(api_key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

documents = [
    "Microsoft,""headquartered in Redmond, was founded by Bill Gates and Paul Allen.",
    "Pichai Sundararajan, better known as Sundar Pichai, is an Indian-born American business executive. He is the chief executive officer of Alphabet Inc. and its subsidiary Google. Pichai began his career as a materials engineer.",
]

response = text_analytics_client.recognize_entities(documents)

for idx, document in enumerate(response):
    print(f"Document {idx + 1}:")
    for entity in document.entities:
        print(f" - Entity: {entity.text}, Type: {entity.category}, "
              f"Subtype: {entity.subcategory}, Confidence Score: {entity.confidence_score}")
