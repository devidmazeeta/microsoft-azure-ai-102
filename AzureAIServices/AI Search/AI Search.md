## 🔍 What is Azure AI Search?

Azure AI Search (formerly Azure Cognitive Search) is a **cloud-based search service** that enables **AI-powered content indexing and search** for applications. It supports full-text search, filters, AI enrichment (OCR, NLP), scoring, and more.

---

## 📚 Core Topics with Python Code and Expected Output

---

### 1. 🔧 Create a Search Index

#### 🧠 Concept:
- Indexes are schemas like tables in a database.
- Fields can be searchable, filterable, sortable, etc.

#### ✅ Python Code:

```python
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes.models import *

endpoint = "https://<your-search-service>.search.windows.net"
admin_key = "<your-admin-key>"

index_client = SearchIndexClient(endpoint=endpoint,
                                 credential=AzureKeyCredential(admin_key))

fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="title", type=SearchFieldDataType.String),
    SearchableField(name="content", type=SearchFieldDataType.String),
    SimpleField(name="category", type=SearchFieldDataType.String, filterable=True),
]

index = SearchIndex(name="sample-index", fields=fields)
result = index_client.create_index(index)
print(f"Index '{result.name}' created.")
```

#### 💬 Output:
```
Index 'sample-index' created.
```

---

### 2. 📥 Create a Data Source (e.g., from Azure Blob)

#### 🧠 Concept:
- Defines where the data comes from (Blob, Cosmos DB, etc.).

#### ✅ Python Code:

```python
from azure.search.documents.indexes.models import SearchIndexerDataSourceConnection

data_source = SearchIndexerDataSourceConnection(
    name="sample-datasource",
    type="azureblob",
    connection_string="DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net",
    container={"name": "sample-container"}
)

index_client.create_data_source_connection(data_source)
print("Data source created.")
```

#### 💬 Output:
```
Data source created.
```

---

### 3. 🛠️ Create an Indexer

#### 🧠 Concept:
- Connects your data source to your index.
- Extracts and loads data periodically.

#### ✅ Python (REST API):

```python
import requests, json

url = f"{endpoint}/indexers/sample-indexer?api-version=2023-11-01"
headers = {
    'Content-Type': 'application/json',
    'api-key': admin_key
}

indexer_config = {
  "name": "sample-indexer",
  "dataSourceName": "sample-datasource",
  "targetIndexName": "sample-index",
  "schedule": { "interval": "PT2H" }
}

response = requests.put(url, headers=headers, json=indexer_config)
print("Indexer status:", response.status_code)
print("Response:", response.json())
```

#### 💬 Output:
```
Indexer status: 201
Response: {'@odata.context': '...', 'name': 'sample-indexer', ...}
```

---

### 4. 🔍 Search the Index

#### 🧠 Concept:
- Retrieve documents using keyword queries.

#### ✅ Python Code:

```python
from azure.search.documents import SearchClient

search_client = SearchClient(endpoint=endpoint,
                             index_name="sample-index",
                             credential=AzureKeyCredential(admin_key))

results = search_client.search("Azure AI")

for result in results:
    print(f"Title: {result['title']} - Category: {result['category']}")
```

#### 💬 Output (Sample):
```
Title: Introduction to Azure AI - Category: Cloud
Title: Cognitive Services Overview - Category: AI
```

---

### 5. 🤖 Add a Skillset for AI Enrichment

#### 🧠 Concept:
- Apply AI models during indexing (OCR, sentiment, key phrases, etc.)

#### ✅ Sample Skillset (REST):

```python
skillset = {
  "name": "demo-skillset",
  "skills": [
    {
      "@odata.type": "#Microsoft.Skills.Text.EntityRecognitionSkill",
      "name": "#1",
      "inputs": [{"name": "text", "source": "/document/content"}],
      "outputs": [{"name": "persons", "targetName": "people"}]
    }
  ]
}

response = requests.put(
    f"{endpoint}/skillsets/demo-skillset?api-version=2023-11-01",
    headers=headers,
    json=skillset
)

print("Skillset created:", response.status_code)
```

#### 💬 Output:
```
Skillset created: 201
```

---

### 6. 🎯 Add Scoring Profile

#### 🧠 Concept:
- Boost specific fields to influence relevance of search results.

#### ✅ Python Code:

```python
scoring_profile = ScoringProfile(
    name="boostTitle",
    text_weights=TextWeights(weights={"title": 3.0})
)

index = index_client.get_index("sample-index")
index.scoring_profiles = [scoring_profile]

index_client.create_or_update_index(index)
print("Scoring profile added.")
```

#### 💬 Output:
```
Scoring profile added.
```

---

### 7. 🔁 Add Synonym Map

#### 🧠 Concept:
- Helps with related term matching, e.g., “car = vehicle”

#### ✅ Python Code:

```python
from azure.search.documents.indexes.models import SynonymMap

synonym_map = SynonymMap(name="car-synonyms", synonyms="car, automobile, vehicle")

index_client.create_synonym_map(synonym_map)
print("Synonym map created.")
```

#### 💬 Output:
```
Synonym map created.
```

---

### 8. 🔐 Authentication Options

- Use **Admin Key** (shown above) for simplicity.
- **Recommended:** Use **Azure Identity** with Azure AD for production.

---

### 9. 📈 Monitor Indexer Status

✅ Sample to check indexer status:

```python
url = f"{endpoint}/indexers/sample-indexer/status?api-version=2023-11-01"
response = requests.get(url, headers=headers)
print(response.json())
```

#### 💬 Output:
```
{
  "lastResult": {
    "status": "success",
    "itemsProcessed": 100,
    "errors": []
  }
}
```

---

## 🧪 Final Use Case (AI Knowledge Search)

Imagine: You have PDFs in Azure Blob:
1. OCR extracts text.
2. Sentiment and key phrases are pulled.
3. Indexed with filters.
4. Searchable by relevance, keyword, or AI-enriched metadata.

---

## 🧰 Setup Requirements

- Azure subscription
- Azure AI Search service
- Blob storage (for input)
- Python 3
- Install libraries:

```bash
pip install azure-search-documents azure-core azure-identity requests
```

---

