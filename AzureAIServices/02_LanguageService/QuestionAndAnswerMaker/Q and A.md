# Microsoft Azure AI Service - QnA Maker

## Introduction
Azure QnA Maker is a cloud-based service that enables developers to create a knowledge base (KB) of question-and-answer pairs. It helps in building conversational AI experiences by extracting structured Q&A content from sources such as FAQs, product manuals, and documents. The QnA Maker service integrates easily with Azure Bot Service, making it a popular choice for chatbots and virtual assistants.

### **Key Features**
- **Natural Language Processing (NLP)**: Understands user queries and fetches the most relevant response.
- **Custom Knowledge Base**: Allows users to create, edit, and manage Q&A pairs.
- **Multi-language Support**: Supports multiple languages for international applications.
- **Easy Integration**: Works seamlessly with Azure Bot Service and other AI tools.
- **Active Learning**: Improves response accuracy by suggesting new questions.

---

## **How QnA Maker Works**
1. **Create a Knowledge Base (KB)**
   - Define question-and-answer pairs manually or extract them from existing content.
2. **Train the Model**
   - Train the AI model to improve response accuracy.
3. **Publish the KB**
   - Make the KB accessible via an API.
4. **Integrate with Applications**
   - Connect with chatbots, websites, or apps.

---

## **Setting Up QnA Maker in Azure**
### **Step 1: Create an Azure QnA Maker Service**
1. Sign in to the [Azure Portal](https://portal.azure.com/).
2. Search for "QnA Maker" and create a new service.
3. Choose a resource group and configure pricing details.
4. Deploy and note the endpoint, subscription key, and knowledge base ID.

### **Step 2: Create a Knowledge Base**
1. Go to the [QnA Maker Portal](https://www.qnamaker.ai/).
2. Sign in with your Azure account.
3. Click "Create a knowledge base."
4. Link it to the Azure QnA Maker service.
5. Add question-answer pairs manually or import an FAQ URL/document.
6. Save and train the KB.

### **Step 3: Deploy and Test**
1. After training, publish the KB.
2. Use the provided API endpoint for integration.

---

## **Python Code Example**
To interact with QnA Maker using Python, we will:
1. Send a question to the QnA Maker API.
2. Receive the best-matching answer.

### **Install Required Libraries**
```python
import requests
import json
```

### **Set Up API Endpoint and Key**
```python
# Replace with your actual endpoint and keys
QNAMAKER_ENDPOINT = "https://your-qna-maker-endpoint.azurewebsites.net/qnamaker"
KNOWLEDGE_BASE_ID = "your-knowledge-base-id"
SUBSCRIPTION_KEY = "your-subscription-key"

# Endpoint for querying the knowledge base
QUERY_URL = f"{QNAMAKER_ENDPOINT}/knowledgebases/{KNOWLEDGE_BASE_ID}/generateAnswer"
```

### **Function to Ask Questions**
```python
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
```

---

## **Use Cases**
### 1️⃣ **Chatbots for Customer Support**
- Automate responses to frequently asked questions.
- Reduce customer service costs.
- Provide instant answers to users.

**Example**: A company can integrate Azure QnA into a chatbot to help customers find product details.

---

### 2️⃣ **Enterprise Knowledge Base**
- Employees can quickly search for company policies, HR guidelines, and IT troubleshooting steps.
- Saves time by automating internal documentation queries.

**Example**: HR chatbot that answers employees' payroll, leave, and benefits queries.

---

### 3️⃣ **E-learning and Educational Platforms**
- Students can ask questions related to course material.
- Supports interactive learning by retrieving answers from textbooks and PDFs.

**Example**: An online coding school integrates QnA with course content, allowing students to ask "How does a for-loop work in Python?" and get instant answers.

---

### 4️⃣ **Healthcare and Medical Support**
- Helps patients find symptoms, treatments, or appointment details.
- Reduces the workload on human medical representatives.

**Example**: A hospital integrates QnA for patients to ask about symptoms before scheduling an appointment.

---

### 5️⃣ **E-commerce Product Assistance**
- Provides instant product recommendations and troubleshooting help.
- Reduces support tickets by answering common questions.

**Example**: An online shopping assistant that answers "How do I return a product?" or "Does this phone support 5G?".

---
## **Sample Knowledge Base (KB)**

1. **EdTech Support Bot** – for answering student and faculty queries  
2. **Retail Product Assistant** – for answering questions related to products in an e-commerce platform

---

### 📘 **Knowledge Base 1: EdTech Support Bot**

| **Question** | **Answer** | **Metadata** |
|--------------|------------|--------------|
| How do I reset my Ednue student password? | To reset your password, go to the login page and click "Forgot Password". Follow the instructions sent to your registered email. | category=account |
| Can I reschedule my exam? | Yes, you can request a reschedule through the student portal under "Exam > Reschedule". Approval is based on your academic guidelines. | category=exam |
| What is the passing criteria for Python certification? | You need to score a minimum of 60% in both the MCQ and coding test sections. | category=certification |
| How do I contact my mentor? | You can message your mentor through the Ednue dashboard or email them directly from the "Mentor" tab. | category=support |
| Are classes recorded? | Yes, all classes are recorded and uploaded within 24 hours. Access them under "My Courses > Recordings". | category=course |

---

### 📘 **Knowledge Base 2: Retail Product Assistant**

| **Question** | **Answer** | **Metadata** |
|--------------|------------|--------------|
| What is the return policy? | You can return products within 7 days of delivery. Ensure the product is unused and in original packaging. | category=policy |
| Is this shirt available in size L? | Please select the size from the product page. If it is not selectable, it's currently out of stock. | category=product_availability |
| How long does delivery take? | Standard delivery takes 3–5 business days depending on your location. | category=shipping |
| Do you offer cash on delivery? | Yes, cash on delivery is available for orders under ₹5000. | category=payment |
| How do I track my order? | Go to "My Orders" and click "Track Order" next to your item. You'll see real-time updates. | category=order_tracking |

---

## **Advanced Features**
- **Multi-Turn Conversations**: Keeps track of previous interactions for a more natural conversation flow.
- **Active Learning**: Improves the model by suggesting new question-answer pairs based on user input.
- **Integration with Power Automate**: Automate workflows by connecting the QnA service to other Microsoft tools.

---

## **Integration with Azure Bot Service**
To make QnA Maker accessible via a chatbot, follow these steps:
1. **Create an Azure Bot Service** and select QnA Maker as the knowledge source.
2. **Configure Bot Channels** (e.g., Microsoft Teams, Web Chat, Slack).
3. **Deploy and Test** the chatbot.

```python
from botbuilder.core import BotFrameworkAdapter
from botbuilder.ai.qna import QnAMaker, QnAMakerEndpoint

# Set up QnA Maker endpoint
qna_maker = QnAMaker(
    QnAMakerEndpoint(
        knowledge_base_id=KNOWLEDGE_BASE_ID,
        endpoint_key=SUBSCRIPTION_KEY,
        host=QNAMAKER_ENDPOINT
    )
)
```

---

## **Conclusion**
Azure QnA Maker is a powerful tool for building intelligent Q&A systems. With its NLP capabilities and easy integration options, it simplifies the creation of AI-driven conversational agents. Whether for customer support, HR, or healthcare, QnA Maker enhances user engagement and automates responses efficiently.
