# **Microsoft Azure AI Document Intelligence (Formerly Azure Form Recognizer)**  

**Azure AI Document Intelligence** is a cloud-based AI service that extracts structured data from documents such as **invoices, receipts, business cards, and identity documents**. It leverages **machine learning and OCR (Optical Character Recognition)** to process and analyze documents efficiently.

---

## **Key Features**
1. **Prebuilt Models** – Extracts data from common document types like invoices, receipts, and ID cards.
2. **Custom Models** – Train AI models for your specific document layout.
3. **OCR and Key-Value Extraction** – Recognizes printed and handwritten text.
4. **Table Extraction** – Detects and extracts tabular data from structured forms.
5. **Multi-Language Support** – Works with multiple languages.
6. **API & SDK Integration** – Easily integrate with applications using REST API and SDKs (Python, C#, Java).

---

## **Use Cases**
- **Invoice Processing**: Extract invoice numbers, amounts, and vendor details.
- **Receipt Processing**: Capture purchase details from receipts automatically.
- **Identity Document Verification**: Extract names, dates of birth, and ID numbers from passports, licenses, and IDs.
- **Business Card Scanning**: Convert business cards into digital contacts.
- **Custom Document Processing**: Train AI models to extract domain-specific information.

---

## **Document & Image Requirements for Azure AI Document Intelligence**  

When using **Azure AI Document Intelligence**, it is important to follow the **document and image format guidelines** to ensure accurate extraction of data. Below are the supported file formats, size limits, and quality recommendations.

---

### **1. Supported File Formats**  
✅ **Images**  
- JPEG / JPG  
- PNG  
- BMP  
- TIFF  

✅ **Documents**  
- PDF (must be text-based or image-based)  
- TIFF (Multipage TIFF is supported)  

⚠ **Unsupported formats**: Word documents (.docx), Excel files (.xlsx), and encrypted/password-protected PDFs are **not supported**.

---

### **2. File Size Limits**  
- **Maximum file size:** **50 MB**  
- **Maximum image dimensions:** **10,000 x 10,000 pixels**  
- **Minimum image dimensions:** **50 x 50 pixels**  
- **PDF page limit:** **2000 pages per document**  

⚠ **Tip**: For large PDFs, **only the first 200 pages** will be analyzed.

---

### **3. Image Quality Recommendations**  
📌 **Resolution & DPI**  
- **Recommended DPI:** **300 DPI or higher** for best OCR accuracy.  
- **Minimum DPI:** **≥150 DPI** (lower DPI may reduce recognition accuracy).  

📌 **Lighting & Contrast**  
- Ensure **good lighting** (avoid shadows or glare).  
- Use a **clear, high-contrast** background.  

📌 **Text Orientation**  
- Documents should be **properly aligned** (avoid tilted or rotated text).  
- If the text is **sideways or upside down**, the model may still recognize it, but accuracy could be lower.

📌 **Handwritten vs. Printed Text**  
- **Handwritten text is supported** but should be **clear and legible**.  
- Printed text has **higher accuracy** than handwritten text.

📌 **Scanned vs. Photographed Documents**  
- **Scanned documents provide the best accuracy** since they are flat and have no distortions.  
- **Photographed documents may cause issues** if they are blurry, distorted, or poorly lit.

---

### **4. Document Structure Recommendations**  
✅ **For Forms, Tables, and Key-Value Extraction**  
- Ensure tables and fields are **clearly structured and not overlapping**.  
- Forms should have **consistent layouts** across multiple documents for best results.  

✅ **For Business Cards & Receipts**  
- Business cards should have **clear text with minimal background noise**.  
- Receipts should be **flat and undamaged** for better extraction.

---

### **5. Examples of Good vs. Bad Document Quality**  

| **Good Example** | **Bad Example** |
|-----------------|----------------|
| ✅ Clear, high-resolution scan | ❌ Blurry, low-resolution image |
| ✅ Proper lighting, no shadows | ❌ Dark lighting, uneven brightness |
| ✅ Text is straight & aligned | ❌ Text is rotated or tilted |
| ✅ High-contrast background | ❌ Noisy background with patterns |
| ✅ Handwritten text is neat | ❌ Handwriting is messy or unclear |

---

# **Step 1: Create an Azure AI Document Intelligence Resource in Azure Portal**
### **1.1 Log in to Azure Portal**
Go to [Azure Portal](https://portal.azure.com) and sign in with your Azure account.

### **1.2 Create a New Resource**
1. Click **"Create a resource"** in the left menu.
2. Search for **"Azure AI Document Intelligence"** (formerly Form Recognizer).
3. Click **"Create"**.

### **1.3 Configure the Resource**
- **Subscription**: Choose your Azure subscription.
- **Resource Group**: Select an existing group or create a new one.
- **Region**: Choose a data center location.
- **Name**: Provide a unique name for the AI Document Intelligence resource.
- **Pricing Tier**: Choose the suitable plan. The **free tier (F0)** allows limited transactions per month.

### **1.4 Review and Deploy**
- Click **"Review + Create"**.
- Once validation passes, click **"Create"**.
- Wait for deployment to complete and then click **"Go to resource"**.

---

# **Step 2: Get API Endpoint and Keys**
After creating the resource:
1. Open your **Azure AI Document Intelligence resource**.
2. Navigate to **Keys and Endpoint**.
3. Copy the **Endpoint** and **API Key** – required for API integration.

---

# **Step 3: Try AI Document Analysis in Azure Portal**
1. Open your **Azure AI Document Intelligence** resource.
2. Click **"Try it"** in the left panel.
3. Select a **prebuilt model** (e.g., Invoice, Receipt, Business Card).
4. Upload a sample document (PDF or image).
5. Click **"Run analysis"** to see extracted data.

---

# **Step 4: Implement in Python**
### **4.1 Install Azure SDK**
```bash
pip install azure-ai-formrecognizer
```

### **4.2 Import Required Libraries**
```python
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os
```

### **4.3 Configure Azure Credentials**
Replace `your-endpoint` and `your-api-key` with your Azure credentials.

```python
# Azure credentials
AZURE_FORM_RECOGNIZER_ENDPOINT = "https://your-resource-name.cognitiveservices.azure.com/"
AZURE_FORM_RECOGNIZER_KEY = "your-api-key"

document_analysis_client = DocumentAnalysisClient(
    endpoint=AZURE_FORM_RECOGNIZER_ENDPOINT,
    credential=AzureKeyCredential(AZURE_FORM_RECOGNIZER_KEY)
)
```

---

# **Step 5: Extract Text from a Document (Invoice Example)**
```python
document_path = "invoice.pdf"  # Path to your document

with open(document_path, "rb") as document_file:
    poller = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-invoice",  # Using the prebuilt invoice model
        document=document_file
    )
    result = poller.result()

# Display extracted information
for idx, field in enumerate(result.documents):
    print(f"Document {idx + 1}")
    for name, value in field.fields.items():
        print(f"{name}: {value.value} (Confidence: {value.confidence})")
```

---

# **Step 6: Extract Data from a Receipt**
```python
with open("receipt.jpg", "rb") as document_file:
    poller = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-receipt",
        document=document_file
    )
    result = poller.result()

# Display receipt details
for receipt in result.documents:
    print(f"Merchant: {receipt.fields.get('MerchantName').value}")
    print(f"Transaction Date: {receipt.fields.get('TransactionDate').value}")
    print(f"Total Amount: {receipt.fields.get('Total').value}")
```

---

# **Step 7: Train a Custom Model (Optional)**
If your documents have a unique format, you can **train a custom model**.

### **7.1 Upload Labeled Data**
1. Upload labeled documents to **Azure Blob Storage**.
2. Get the **Storage Container URL**.

### **7.2 Train the Custom Model**
```python
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
```

### **7.3 Use the Custom Model**
```python
with open("custom-document.jpg", "rb") as document_file:
    poller = document_analysis_client.begin_analyze_document(
        model_id="your-custom-model-id",
        document=document_file
    )
    result = poller.result()

for field_name, field_value in result.documents[0].fields.items():
    print(f"{field_name}: {field_value.value} (Confidence: {field_value.confidence})")
```

---

# **Step 8: Deploy and Monitor**
### **8.1 Integrate with Applications**
- Deploy in **Power Automate, Power Apps, or Web Apps**.
- Use **REST API** for real-time document analysis.

### **8.2 Monitor Usage**
- Navigate to **Metrics** in Azure Portal to track API usage and performance.

---

# **Conclusion**
Azure AI Document Intelligence is a powerful tool for **automated document processing**. It extracts **structured data** from invoices, receipts, and custom forms, reducing **manual effort**. 

