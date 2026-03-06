# 🧠 DocuMind AI — RAG Chatbot

DocuMind AI is a Retrieval-Augmented Generation (RAG) chatbot that answers user queries by retrieving relevant information from custom documents and generating intelligent responses using Large Language Models.

This project combines **semantic search** with **LLM reasoning** to provide accurate, context-aware answers from your own data.

---

## 🚀 Features

• 📄 Document-based Question Answering
• 🔎 Semantic Search using FAISS Vector Store
• 🤗 Hugging Face Embeddings & LLM Integration
• ⚡ Fast Retrieval with Local Vector Database
• 🔐 Secure API Key Management using .env
• 💻 Simple Python-based Architecture

---

## 🏗️ Project Structure

```
DocuMind_AI_RagChatBot
│
├── data/                # Source documents
├── vectors/             # Stored FAISS vector database
├── qa.py                # Main Q&A pipeline
├── ingest.py            # Document processing & embedding
├── frontapp.py          # Frontend interface
├── requirements.txt     # Project dependencies
├── .env                 # API keys (not uploaded to GitHub)
└── README.md            # Project documentation
```

---

## ⚙️ How It Works

1️⃣ Documents are processed and converted into embeddings
2️⃣ Embeddings are stored in a FAISS vector database
3️⃣ User query is converted into an embedding
4️⃣ Similar document chunks are retrieved
5️⃣ LLM generates a final answer using retrieved context

This improves accuracy and reduces hallucinations.

---

## 🧰 Tech Stack

**Language:** Python
**Frameworks & Libraries:**

* LangChain
* FAISS
* HuggingFace Transformers
* SentenceTransformers
* Python-dotenv

---

## 🔑 Environment Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/DocuMind_AI_RagChatBot.git
cd DocuMind_AI_RagChatBot
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add API Key

Create `.env` file:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key_here
```

---

## ▶️ Running the Project

### Step 1 — Process Documents

```bash
python ingest.py
```

### Step 2 — Start Chatbot

```bash
python frontapp.py
```

---

## 💡 Use Cases

• Research Paper Assistance
• College Notes Q&A
• Medical Document Search
• Legal Document Analysis
• Company Knowledge Base Chatbot

---

## 📌 Future Improvements

• Web deployment
• Multi-document upload
• Chat history memory
• Voice-enabled interface
• Support for more LLM providers

---
## ⭐ Support

If you found this project helpful, please give it a star on GitHub!
# DocuMind_AI_RagChatBot
