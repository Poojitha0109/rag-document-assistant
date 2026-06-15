# 📄 PDF RAG Chat with LangChain, ChromaDB & Gemini

A Retrieval-Augmented Generation (RAG) application that enables semantic search and question-answering over PDF documents using LangChain, ChromaDB, HuggingFace Embeddings, and Google Gemini.

## 🚀 Features

* Load and parse PDF documents
* Split documents into semantic chunks
* Generate vector embeddings
* Store embeddings in ChromaDB
* Perform semantic similarity search
* Retrieve relevant document context
* Generate grounded answers using Gemini
* Support for querying resumes, handbooks, policies, and other PDF documents

## 🏗️ Architecture

```text
PDF Document
      ↓
Document Loader
      ↓
Text Chunking
      ↓
Embeddings
      ↓
ChromaDB Vector Store
      ↓
Similarity Search
      ↓
Retrieved Context
      ↓
Gemini LLM
      ↓
Answer
```

## 🖥️ Web Interface

Users can:

- Upload PDF documents
- Ask questions in a chat interface
- Receive AI-generated answers grounded in document context
- Interact with documents using Retrieval-Augmented Generation (RAG)

### Architecture

PDF Upload
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Similarity Search
↓
Gemini
↓
Answer Generation

## 🛠️ Tech Stack

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Google Gemini
* PyPDF
* Sentence Transformers

## 📂 Project Structure

```text
rag-demo/
│
├── data/
│   └── handbook.pdf
│
├── db/
│
├── main.py
│
├── .env
│
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/pdf-rag-chat.git

cd pdf-rag-chat
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

## ▶️ Run the Application

```bash
python main.py
```

Example query:

```text
How many PTO days do employees receive?
```

Example response:

```text
Employees receive 20 paid time off (PTO) days per calendar year.
```

## 📚 What I Learned

Through this project I gained hands-on experience with:

* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Embedding Models
* Document Chunking Strategies
* Context Grounding
* LLM Integration
* AI Application Architecture

## 🔮 Future Improvements

* FastAPI Backend
* Angular Frontend
* Multi-PDF Support
* Source Citations
* Conversation Memory
* AWS Deployment
* Authentication & User Uploads

## 👩‍💻 Author

Poojitha Panabaka

Software Engineer | Java | Python | Angular | AWS | AI Engineering

LinkedIn:
https://www.linkedin.com/in/panabakapoojitha/

---

Built while learning Retrieval-Augmented Generation (RAG), LLMs, and Applied AI Engineering.
