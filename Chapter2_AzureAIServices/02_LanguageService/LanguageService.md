### **Comprehensive Microsoft Azure AI Language Documentation with Python Examples**

---

### **Overview**

Microsoft Azure AI Language provides a suite of natural language processing (NLP) tools that allow developers to analyze and process text or spoken languages. This service offers capabilities such as sentiment analysis, key phrase extraction, named entity recognition, and more.

Azure AI Language services can be accessed using Python SDKs or REST APIs. This documentation combines an overview of features with detailed Python code examples.

---

### **Key Features**

1. **Text Analytics**:
   - Sentiment Analysis
   - Key Phrase Extraction
   - Named Entity Recognition (NER)
   - Language Detection

2. **Language Understanding (LUIS)**:
   - Custom language models to recognize intents and entities.
   - Prebuilt intents and entities for common use cases.

3. **Conversation Analysis**:
   - Analyze customer-agent interactions to gain actionable insights.

4. **Question Answering**:
   - Build intelligent Q&A systems from existing documents or FAQs.

5. **Custom NLP Models**:
   - Train domain-specific models for text classification or named entity recognition.

---

### **Setup**

#### **Step 1: Create an Azure AI Language Resource**

1. Go to the [Azure Portal](https://portal.azure.com).
2. Select **Create a Resource** > **AI + Machine Learning** > **Language**.
3. Configure your resource:
   - Subscription: Choose your Azure subscription.
   - Resource Group: Create or select an existing group.
   - Region: Choose a suitable region.
   - Pricing Tier: Select the pricing tier that fits your needs.

#### **Step 2: Install Required Python Libraries**

```bash
pip install azure-ai-textanalytics
```

#### **Step 3: Authenticate the Client**

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Replace with your Azure resource credentials
endpoint = "https://<your-resource-name>.cognitiveservices.azure.com/"
api_key = "<your-api-key>"

# Initialize the client
credential = AzureKeyCredential(api_key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)
```

---

### **Core Features and Python Examples**

#### **1. Sentiment Analysis**

Analyze the sentiment (positive, neutral, or negative) of input text.

```python
# Input text
documents = [
    "I absolutely love using Azure AI for natural language processing tasks!"
]

# Call the sentiment analysis API
response = text_analytics_client.analyze_sentiment(documents)

# Process and display the results
for idx, document in enumerate(response):
    print(f"Document {idx + 1}: Sentiment = {document.sentiment}")
    print(f"Confidence Scores: Positive = {document.confidence_scores.positive}, "
          f"Neutral = {document.confidence_scores.neutral}, "
          f"Negative = {document.confidence_scores.negative}")
```

**Sample Output**:
```
Document 1: Sentiment = positive
Confidence Scores: Positive = 0.98, Neutral = 0.01, Negative = 0.01
```

---

#### **2. Key Phrase Extraction**

Extract important key phrases from text to identify main topics or themes.

```python
documents = [
    "Azure AI provides powerful tools for developers to build intelligent applications."
]

response = text_analytics_client.extract_key_phrases(documents)

for idx, document in enumerate(response):
    print(f"Document {idx + 1}: Key Phrases = {', '.join(document.key_phrases)}")
```

**Sample Output**:
```
Document 1: Key Phrases = Azure AI, powerful tools, intelligent applications
```

---

#### **3. Named Entity Recognition (NER)**

Identify entities such as names, organizations, dates, or locations.

```python
documents = [
    "Microsoft, headquartered in Redmond, was founded by Bill Gates and Paul Allen."
]

response = text_analytics_client.recognize_entities(documents)

for idx, document in enumerate(response):
    print(f"Document {idx + 1}:")
    for entity in document.entities:
        print(f" - Entity: {entity.text}, Type: {entity.category}, "
              f"Subtype: {entity.subcategory}, Confidence Score: {entity.confidence_score}")
```

**Sample Output**:
```
Document 1:
 - Entity: Microsoft, Type: Organization, Subtype: None, Confidence Score: 0.99
 - Entity: Redmond, Type: Location, Subtype: City, Confidence Score: 0.98
 - Entity: Bill Gates, Type: Person, Subtype: None, Confidence Score: 0.99
 - Entity: Paul Allen, Type: Person, Subtype: None, Confidence Score: 0.99
```

---

#### **4. Language Detection**

Detect the language of input text.

```python
documents = [
    "Bonjour, comment ça va ?",
    "This is a sample English sentence."
]

response = text_analytics_client.detect_language(documents)

for idx, document in enumerate(response):
    print(f"Document {idx + 1}: Language = {document.primary_language.name}, "
          f"ISO Code = {document.primary_language.iso6391_name}")
```

**Sample Output**:
```
Document 1: Language = French, ISO Code = fr
Document 2: Language = English, ISO Code = en
```

---

#### **5. Custom NLP Models**

Train domain-specific models to classify text or recognize custom entities.

```python
endpoint = "https://<your-custom-model-endpoint>.cognitiveservices.azure.com/"
api_key = "<your-api-key>"

custom_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

documents = ["Identify this custom entity: Order ID 12345"]

response = custom_client.recognize_entities(documents)

for idx, document in enumerate(response):
    print(f"Document {idx + 1}:")
    for entity in document.entities:
        print(f" - Entity: {entity.text}, Type: {entity.category}, Confidence Score: {entity.confidence_score}")
```

---

### **Error Handling**

Handle exceptions for robust application development.

```python
from azure.core.exceptions import HttpResponseError

try:
    documents = ["This is an example for error handling."]
    response = text_analytics_client.analyze_sentiment(documents)
    for document in response:
        print(f"Sentiment: {document.sentiment}")

except HttpResponseError as e:
    print(f"Error: {e.message}")
```

---

### **Resources**

- [Azure AI Python SDK Documentation](https://learn.microsoft.com/en-us/python/api/overview/azure/ai-textanalytics-readme)
- [Azure AI Language Service Quickstart](https://learn.microsoft.com/en-us/azure/ai-language/)
- [LUIS Portal](https://www.luis.ai/)

---

### **Best Practices**

1. **Batch Processing**:
   - Combine multiple documents into a single API call to reduce latency and cost.
   
2. **Use Appropriate Models**:
   - Leverage prebuilt models for common scenarios or train custom models for domain-specific tasks.

3. **Caching**:
   - Cache results for frequently analyzed data to reduce repetitive API calls.

4. **Error Handling**:
   - Implement robust error handling to handle rate limits and invalid inputs.

---

This consolidated documentation covers both the features and Python implementation of Microsoft Azure AI Language services, providing a complete guide to build intelligent NLP solutions.