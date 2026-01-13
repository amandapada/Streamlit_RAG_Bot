# Customer Support Bot Demo

An intelligent customer support chatbot built with **Streamlit** and **LlamaIndex**, powered by **Google Gemini AI**. The bot uses Retrieval-Augmented Generation (RAG) to answer customer queries based on your organization's knowledge base documents.

---

## Features

- **RAG-Powered Responses** – Answers questions using your own knowledge base documents
- **Conversational Interface** – Natural chat experience with conversation history
- **Smart Escalation** – Automatically redirects sensitive queries to human support
- **Knowledge Base Refresh** – Reload documents without restarting the app
- **Google Gemini Integration** – Utilizes Gemini 2.5 Flash for intelligent responses

---

## Project Structure

```
Customer_enquiry_bot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── .streamlit/
│   └── secrets.toml      # API keys and secrets (not tracked in git)
├── data/                 # Knowledge base documents
│   ├── OFFICE HOURS & FACILITIES FAQ.txt
│   ├── SECURITY GUIDELINES.txt
│   └── VISITOR POLICY.txt
└── venv/                 # Python virtual environment
```

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- A Google AI Studio API key ([Get one here](https://aistudio.google.com/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Customer_enquiry_bot
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**
   
   Create a file at `.streamlit/secrets.toml` and add your Gemini API key:
   ```toml
   GEMINI_API_KEY = "your-api-key-here"
   ```

5. **Add your knowledge base documents**
   
   Place your `.txt`, `.pdf`, or other supported document files in the `data/` folder. The bot will automatically index them on startup.

### Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Customization

### Adding Documents

Simply add your documents to the `data/` folder. Supported formats include:
- `.txt` (Plain text)
- `.pdf` (PDF documents)
- `.docx` (Word documents)
- And more (see [LlamaIndex documentation](https://docs.llamaindex.ai/en/stable/module_guides/loading/simpledirectoryreader/))

### Modifying the System Prompt

Edit the `Settings.system_prompt` in `app.py` to customize how the bot responds:

```python
Settings.system_prompt = (
    "You are a customer support assistant. Follow these rules:\n"
    "1. If the question can be answered from the knowledge base, provide a clear answer\n"
    "2. If it requires account access, payments, or sensitive info, say: 'I'll connect you with our team at support@techub.com'\n"
    "3. If uncertain, ask clarifying questions\n"
    "4. Always be friendly and concise"
)
```

---