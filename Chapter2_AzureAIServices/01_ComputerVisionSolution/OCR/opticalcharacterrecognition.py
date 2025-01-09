import os
import time
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
from uuid import UUID

# Add your Computer Vision key and endpoint
key = os.getenv("VISION_KEY")
endpoint = os.getenv("VISION_ENDPOINT")

READ_TEXT_URL_IMAGE = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/printed_text.jpg"

def main():
    print("Azure Cognitive Services Computer Vision")
    print()

    client = authenticate(endpoint, key)

    # Extract text (OCR) from a URL image using the Read API
    read_file_url(client, READ_TEXT_URL_IMAGE)

def authenticate(endpoint, key):
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
    return client

def read_file_url(client, url_file):
    print("----------------------------------------------------------")
    print("READ FILE FROM URL")
    print()

    # Read text from URL
    text_headers = client.read(url_file, raw=True)
    operation_location = text_headers.headers["Operation-Location"]

    # Retrieve the operation ID
    operation_id = operation_location.split("/")[-1]

    # Wait for the result
    time.sleep(2)
    while True:
        results = client.get_read_result(UUID(operation_id))
        if results.status not in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
            break
        time.sleep(1)

    # Display the found text
    print()
    if results.status == OperationStatusCodes.succeeded:
        for page in results.analyze_result.read_results:
            for line in page.lines:
                print(line.text)
    print()

if __name__ == "__main__":
    main()
