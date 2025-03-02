import openai

openai.api_type = "azure"
openai.api_base = "https://your-resource-name.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "your-api-key"

def chatbot():
    print("Chatbot is running. Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = openai.ChatCompletion.create(
            engine="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        print("Bot:", response["choices"][0]["message"]["content"])

chatbot()
