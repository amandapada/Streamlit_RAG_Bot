import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, ServiceContext
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

# Configure Gemini
llm = GoogleGenAI(
    model="gemini-2.5-flash",  
    api_key=st.secrets["GEMINI_API_KEY"]
)

embed_model = GoogleGenAIEmbedding(
    model_name="text-embedding-004",
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Page config
st.header("Customer Support Bot Demo")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! Ask me anything about our services, or I can redirect you to support."}
    ]

# Load and index knowledge base
@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner("Loading knowledge base..."):
        # Load documents from data/ folder
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        
        Settings.llm = llm
        Settings.embed_model = embed_model 
        Settings.system_prompt = (
                "You are a customer support assistant. Follow these rules:\n"
                "1. If the question can be answered from the knowledge base, provide a clear answer\n"
                "2. If it requires account access, payments, or sensitive info, say: 'I'll connect you with our team at support@techub.com'\n"
                "3. If uncertain, ask clarifying questions\n"
                "4. Always be friendly and concise"
        )
        
        # Index documents
        index = VectorStoreIndex.from_documents(docs)
        return index

index = load_data()

# Create chat engine
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Your question"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            st.session_state.messages.append({"role": "assistant", "content": response.response})

if st.sidebar.button("Refresh Knowledge Base"):
    st.cache_resource.clear()
    st.rerun()