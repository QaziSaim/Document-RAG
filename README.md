# Document RAG Chatbot

A FastAPI-based Retrieval-Augmented Generation (RAG) chatbot that can answer questions from any custom document using LangChain, OpenAI, and FAISS vector search.

This project is designed to work with different types of documents such as:

- PDF files
- Text files
- Research papers
- Notes
- Scripts
- Articles
- Documentation

For testing purposes, this project uses the Pokémon unreleased movie script **Team Rocket vs Team Plasma** as the knowledge source.
---

# Features

- FastAPI backend
- HTML frontend with Jinja2 templates
- LangChain RAG pipeline
- FAISS vector database
- OpenAI Embeddings
- GPT-4o-mini model support
- Pokémon knowledge chatbot
- Simple and clean UI

---

# Project Structure

```bash
project/
│
├── app.py
├── backend.py
├── templates/
│   └── index.html
│
├── vectors/
├── .env
├── requirements.txt
└── README.md
```

---

# Technologies Used

- FastAPI
- LangChain
- OpenAI
- FAISS
- Jinja2
- HTML/CSS
- Python

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd project
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn jinja2 python-multipart
pip install langchain langchain-openai langchain-community
pip install faiss-cpu python-dotenv
```

---

# Environment Variables

Create a `.env` file in the root folder.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open your browser:

```bash
http://127.0.0.1:8000
```

---

# How It Works

1. User enters a question in the frontend.
2. FastAPI sends the query to the backend.
3. FAISS retrieves relevant Pokémon documents.
4. LangChain combines context with the user query.
5. GPT-4o-mini generates the final answer.
6. Response is displayed on the webpage.

---

# Example Questions

- Who is the main villain in Team Rocket vs Team Plasma?
- Tell me about Ash's Pokémon.
- What happened in the unreleased movie?
- Who is Giovanni?
- Explain Team Plasma.

---

# API Endpoint

## GET Request

```bash
/
```

## POST Request

```bash
/
```

Form field:

```bash
query
```

---

# Future Improvements

- Chat history
- Streaming responses
- Dark mode UI
- Pokémon images
- Voice input
- AJAX without page reload
- Authentication system

---

# Screenshot

Add your project screenshot here.

```bash
screenshots/project.png
```

---

# License

This project is for educational purposes.

---

# Author

Your Name