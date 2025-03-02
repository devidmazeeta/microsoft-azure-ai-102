import openai

openai.api_type = "azure"
openai.api_base = "https://your-resource-name.openai.azure.com/"
openai.api_version = "2023-05-15"
openai.api_key = "your-api-key"

response = openai.Image.create(
    model="dall-e-2",
    prompt="A futuristic cityscape at sunset",
    n=1,
    size="1024x1024"
)

print(response["data"][0]["url"])
