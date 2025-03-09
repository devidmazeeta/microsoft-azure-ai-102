import requests
import json

# LUIS Configuration
LUIS_ENDPOINT = "https://<your-luis-endpoint>.cognitiveservices.azure.com/"
LUIS_APP_ID = "<your-luis-app-id>"
LUIS_PREDICTION_KEY = "<your-luis-prediction-key>"

# List of test utterances
utterances = [
    "Book a flight to London next Monday",
    "What’s the weather like in Mumbai today?",
    "Transfer $500 to John's account",
    "Order a large pepperoni pizza for delivery",
    "Schedule a doctor’s appointment for next Friday at 3 PM"
]

def get_luis_prediction(query):
    url = f"{LUIS_ENDPOINT}/luis/prediction/v3.0/apps/{LUIS_APP_ID}/slots/production/predict"
    params = {
        'query': query,
        'subscription-key': LUIS_PREDICTION_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

# Test multiple utterances
for utterance in utterances:
    print(f"\nUser Input: {utterance}")
    result = get_luis_prediction(utterance)
    print(json.dumps(result, indent=4))
