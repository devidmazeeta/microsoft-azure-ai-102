import requests
import json

# Replace with your actual endpoint and keys
QNAMAKER_ENDPOINT = "https://your-qna-maker-endpoint.azurewebsites.net/qnamaker"
KNOWLEDGE_BASE_ID = "your-knowledge-base-id"
SUBSCRIPTION_KEY = "your-subscription-key"

# Endpoint for querying the knowledge base
QUERY_URL = f"{QNAMAKER_ENDPOINT}/knowledgebases/{KNOWLEDGE_BASE_ID}/generateAnswer"


def get_answer_from_qna_maker(question):
    headers = {
        "Authorization": f"EndpointKey {SUBSCRIPTION_KEY}",
        "Content-Type": "application/json"
    }
    payload = json.dumps({"question": question})

    response = requests.post(QUERY_URL, headers=headers, data=payload)

    if response.status_code == 200:
        answer = response.json()["answers"][0]["answer"]
        return answer
    else:
        return f"Error: {response.status_code}, {response.text}"


# Example Query
question = "What is Microsoft Azure?"
answer = get_answer_from_qna_maker(question)
print("Bot's Response:", answer)
