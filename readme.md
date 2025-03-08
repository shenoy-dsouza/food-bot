# 🍔 FoodBot - AI-Powered Food Delivery Assistant

FoodBot is an AI-powered chatbot designed to assist users with their food delivery queries. It leverages **FAISS** for efficient similarity search, **Sentence Transformers** for text embeddings, and **Ollama** for AI-generated responses.

## 🚀 Features

- ✅ **Instant Answers** - Provides quick responses to common food delivery questions.
- 🔍 **Smart Search** - Uses FAISS for fast and relevant FAQ retrieval.
- 🤖 **AI-Powered Responses** - Enhances responses with a conversational AI model.
- 📄 **Easy to Update** - Simply modify `faq.txt` to add new FAQs.
- 🏃️ **Lightweight & Fast** - Uses optimized embeddings for quick searches.

---

## 👥 Installation & Setup

### 1️⃣ Clone the Repository
```bash
   git clone https://github.com/shenoy-dsouza/foodbot.git
   cd foodbot
```

### 2️⃣ Set Up the Virtual Environment
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
   pip install -r requirements.txt
```

---

## 📅 Add Your FAQ Data
Create a `faq.txt` file containing common food delivery questions and answers:
```txt
Q: How do I track my order?
A: Go to "My Orders" in the app to see real-time tracking of your delivery.  

Q: What payment methods do you accept?
A: We accept credit/debit cards, PayPal, and cash on delivery.
```

### ▶️ Run the Chatbot
```bash
python chatbot.py
```

---

## 💡 How It Works

1. **Loads FAQ Data** - Reads `faq.txt` and splits it into chunks.
2. **Generates Embeddings** - Converts FAQ data into numerical embeddings using `SentenceTransformer`.
3. **Stores in FAISS** - Saves embeddings in a FAISS index for fast retrieval.
4. **Retrieves Best Match** - Searches FAISS for the closest match to user input.
5. **Enhances with AI** - Uses `Ollama` to generate a conversational response based on the retrieved FAQ.

---

## 🔥 Example Usage
```bash
🤖 Welcome to FoodBot! Ask about orders, deliveries, payments & more.

User: How do I track my orders?
Bot: You can check the status of your orders by going to "My Orders" in the app, where you'll see real-time tracking information.

User: Do you accept COD?   
Bot: Yes, we do accept Cash On Delivery (COD) in some locations.
```

---

## 🌍 Use Cases
While FoodBot is tailored for **food delivery**, a similar chatbot can be used in:

- 🏥 **Hospitals** - Answer patient queries about appointments and procedures.
- 🎓 **Education** - Provide students with instant academic and administrative information.
- 🛒 **E-Commerce** - Assist customers with order tracking, returns, and product details.
- ✈️ **Travel & Hospitality** - Help travelers with booking, check-in, and FAQs.

---

## 🛠️ Future Enhancements
- 🔄 **Multi-language Support**
- 🎧 **Voice Input Capabilities**
- 📦 **Integration with Live Support Agents**

