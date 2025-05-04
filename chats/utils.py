from .config import get_gemini_model

import re

def format_gemini_response(raw_text):
    # Convert **bold** to <strong> tags
    formatted = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', raw_text)
    # Convert numbered list formatting (optional tweak)
    formatted = re.sub(r'(\d+)\.\s', r'<br>\1. ', formatted)
    # Convert other newlines to <br>
    formatted = formatted.replace('\n', '<br>')
    return formatted


def convert_bpmn_to_nl(xml_content):
    """Sends BPMN XML to Gemini API and gets natural language description."""
    model = get_gemini_model()
    prompt = f"Convert this BPMN XML into a detailed process description:\n{xml_content}"
    
    try:
        response = model.generate_content(prompt)
        return format_gemini_response(response.text)
        # return response.text.strip()
    except Exception as e:
        return f"Error in processing BPM to NLD: {str(e)}"

def generate_query_response(des, query_text):
    """Sends BPMN XML to Gemini API and gets natural language description."""
    model = get_gemini_model()
    prompt = f"this is  context:\n ```{des}```\n\n answer the following query from above\n```{query_text}```"
    
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error in reponsing Query: {str(e)}"



# import requests

# RAG_SERVICE_URL = "http://127.0.0.1:8000/rag"  # Adjust based on your setup

# def convert_bpmn_to_nl(xml_content):
#     """Call the RAG API to convert BPMN XML to natural language."""
#     url = f"{RAG_SERVICE_URL}/bpmn-to-nl/"
#     payload = {"xml_content": xml_content}
    
#     try:
#         response = requests.post(url, json=payload)
#         response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
#         return response.json().get("nl_description", "Failed to generate description")
#     except requests.RequestException as e:
#         print(f"Error in BPMN conversion: {e}")
#         return "Error converting BPMN to NL"


# def generate_query_response(query_text):
#     """Call the RAG API to generate a response using RAG retrieval."""
#     url = f"{RAG_SERVICE_URL}/query/"
#     payload = {"query_text": query_text}
    
#     try:
#         response = requests.post(url, json=payload)
#         response.raise_for_status()
#         return response.json().get("response", "Failed to generate response")
#     except requests.RequestException as e:
#         print(f"Error in query response generation: {e}")
#         return "Error generating query response"
