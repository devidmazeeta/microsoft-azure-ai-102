## **1. Understanding Utterances, Intents & Entities**

| **Concept**  | **Definition** |
|-------------|--------------|
| **Utterance** | A phrase or sentence that a user inputs (e.g., "Book a flight to Paris next Monday") |
| **Intent** | The action that the user wants to perform (e.g., "BookFlightIntent") |
| **Entity** | Specific information extracted from the utterance (e.g., "Paris" as **Location**, "next Monday" as **Date**) |

---

## **2. Examples of Utterances, Intents, and Entities**

### **Example 1: Flight Booking**
| **Utterance** | **Intent** | **Entities Extracted** |
|--------------|-----------|-----------------------|
| "Book a flight to London next Monday" | BookFlightIntent | Location: **London**, Date: **next Monday** |
| "I need a ticket for New York tomorrow" | BookFlightIntent | Location: **New York**, Date: **tomorrow** |
| "Can I fly to Paris this Saturday?" | BookFlightIntent | Location: **Paris**, Date: **this Saturday** |

---

### **Example 2: Weather Inquiry**
| **Utterance** | **Intent** | **Entities Extracted** |
|--------------|-----------|-----------------------|
| "What’s the weather like in Mumbai today?" | GetWeatherIntent | Location: **Mumbai**, Date: **today** |
| "Will it rain in Berlin tomorrow?" | GetWeatherIntent | Location: **Berlin**, Date: **tomorrow**, WeatherType: **rain** |
| "Tell me the temperature in Sydney next weekend" | GetWeatherIntent | Location: **Sydney**, Date: **next weekend** |

---

### **Example 3: Food Ordering**
| **Utterance** | **Intent** | **Entities Extracted** |
|--------------|-----------|-----------------------|
| "Order a large pepperoni pizza for delivery" | OrderFoodIntent | FoodItem: **pepperoni pizza**, Size: **large**, Service: **delivery** |
| "I’d like a medium cheeseburger and fries for pickup" | OrderFoodIntent | FoodItem: **cheeseburger, fries**, Size: **medium**, Service: **pickup** |
| "Can I get a small iced coffee with no sugar?" | OrderFoodIntent | Beverage: **iced coffee**, Size: **small**, Sugar: **no** |

---

### **Example 4: Banking Transactions**
| **Utterance** | **Intent** | **Entities Extracted** |
|--------------|-----------|-----------------------|
| "Transfer $500 to John’s account" | MoneyTransferIntent | Amount: **$500**, Recipient: **John** |
| "Send ₹2000 to my savings account" | MoneyTransferIntent | Amount: **₹2000**, AccountType: **savings** |
| "Move 300 euros from checking to credit card" | MoneyTransferIntent | Amount: **300 euros**, FromAccount: **checking**, ToAccount: **credit card** |

---

### **Example 5: Appointment Scheduling**
| **Utterance** | **Intent** | **Entities Extracted** |
|--------------|-----------|-----------------------|
| "Schedule a doctor’s appointment for next Friday at 3 PM" | ScheduleAppointmentIntent | AppointmentType: **doctor**, Date: **next Friday**, Time: **3 PM** |
| "Book a haircut at 10 AM tomorrow" | ScheduleAppointmentIntent | AppointmentType: **haircut**, Date: **tomorrow**, Time: **10 AM** |
| "Can I meet the lawyer on Monday morning?" | ScheduleAppointmentIntent | AppointmentType: **lawyer**, Date: **Monday**, Time: **morning** |

---

## **3. Python Example with More Utterances**
Let's create a more **advanced** LUIS API request that can handle multiple utterances.

```python
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
```

---

## **4. How LUIS Processes These Utterances**
LUIS will return JSON responses that identify:
- **Top Intent** (highest confidence score)
- **Entities extracted**
- **Confidence Scores** (how sure LUIS is about the intent)

### **Example Response for "Order a large pepperoni pizza for delivery"**
```json
{
    "query": "Order a large pepperoni pizza for delivery",
    "prediction": {
        "topIntent": "OrderFoodIntent",
        "intents": {
            "OrderFoodIntent": {
                "score": 0.98
            }
        },
        "entities": {
            "FoodItem": ["pepperoni pizza"],
            "Size": ["large"],
            "Service": ["delivery"]
        }
    }
}
```

---

## **5. Summary**
| **Concept** | **Description** |
|------------|---------------|
| **Utterances** | What users say (e.g., "Book a flight to New York tomorrow") |
| **Intents** | Actions to be performed (e.g., "BookFlightIntent") |
| **Entities** | Extracted details (e.g., "New York" as Location, "tomorrow" as Date) |
| **LUIS Integration** | Easily integrates with chatbots, apps, and voice assistants |

---

## **Final Thoughts**
- LUIS can **understand human language** and extract meaningful data.
- It is widely used in **chatbots, automation, customer support, and AI applications**.
- By training LUIS with **more utterances, intents, and entities**, it can become **more accurate**.

