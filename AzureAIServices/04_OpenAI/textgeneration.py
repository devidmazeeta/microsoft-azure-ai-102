import openai

openai.api_type = "azure"
openai.api_base = "https://your-resource-name.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "your-api-key"

response = openai.ChatCompletion.create(
    engine="gpt-4",
    messages=[
        {"role": "system", "content": "You are an AI assistant."},
        {"role": "user", "content": "Explain AI in simple terms."}
    ]
)

print(response["choices"][0]["message"]["content"])

# prompt = "You are an expert in AI. Explain the difference between machine learning and deep learning in simple terms."
#
# response = openai.ChatCompletion.create(
#     engine="gpt-4",
#     messages=[
#         {"role": "system", "content": "You are an AI assistant."},
#         {"role": "user", "content": prompt}
#     ]
# )
#
# print(response["choices"][0]["message"]["content"])
