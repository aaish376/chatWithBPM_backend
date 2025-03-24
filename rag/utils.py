from .config import get_gemini_model

def convert_bpmn_to_nl(xml_content):
    """Sends BPMN XML to Gemini API and gets natural language description."""
    model = get_gemini_model()
    prompt = f"Convert this BPMN XML into a detailed process description:\n{xml_content}"
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in processing: {str(e)}"


# from langchain.embeddings import OpenAIEmbeddings

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI


from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.schema import SystemMessage, HumanMessage
from .config import get_gemini_model

# Store descriptions in-memory FAISS for now (later, use a database)
vector_store = None

def store_nl_description(nl_description):
    """Stores the NL description in a vector database (FAISS)."""
    global vector_store
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    texts = text_splitter.split_text(nl_description)
    
    embeddings = OpenAIEmbeddings()  # Replace with Gemini-compatible embeddings if needed
    vector_store = FAISS.from_texts(texts, embeddings)

def generate_query_response(query_text):
    """Uses RAG to generate a response based on stored NL descriptions."""
    global vector_store
    if vector_store is None:
        return "No BPMN data available yet."

    docs = vector_store.similarity_search(query_text, k=3)  # Retrieve top 3 relevant texts
    context = "\n".join([doc.page_content for doc in docs])

    # Use Gemini to generate a response
    model = get_gemini_model()
    prompt = f"Context: {context}\n\nQuestion: {query_text}\nAnswer in detail:"
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in processing: {str(e)}"
