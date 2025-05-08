from .config import get_text_generation_model

def convert_bpmn_to_nl(xml_content):
    """Sends BPMN XML to OpenAI API and gets natural language description."""
    model = get_text_generation_model()
    prompt = f"""
    This is a BPM (Business Process Model): \n ```{xml_content}```\n\n
    Convert this BPMN XML into a detailed process description in layman language 
    without using complex BPMN notations or technical terms.
    Do not add any content beyond what is present in the BPM. Stay within the context of our BPM:\n```{xml_content}```.
    Use HTML formatting for response: <p>, <strong>, <ul>, <li>, <h3>, etc.
    Wrap the entire response in a <div> tag.
    """
    
    try:
        response = model.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error in processing BPM to NLD: {str(e)}"


def generate_query_response(des, query_text):
    """Generates a response to a query using OpenAI API."""
    model = get_text_generation_model()
    prompt = f"""
    This is the context:\n ```{des}```\n\n 
    This is the query: \n ```{query_text}```\n\n
    Answer the query strictly from the given context. 
    - If the query is somehow related to the context but the answer does not exist, say "Answer not found in BPM".
    - If the query is to explain the context, provide a detailed explanation.
    - If the query is irrelevant to the context, say "Irrelevant query".
    Use HTML formatting for response: <p>, <strong>, <ul>, <li>, <h3>, etc.
    Wrap the entire response in a <div> tag.
    """
    
    try:
        response = model.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7
        )
        return response['choices'][0]['text'].strip()
    except Exception as e:
        return f"Error in responding to query: {str(e)}"



# from .config import get_gemini_model


# def convert_bpmn_to_nl(xml_content):
#     """Sends BPMN XML to Gemini API and gets natural language description."""
#     model = get_gemini_model()
#     prompt = f"""
#     This is BPM (Business Process Model): \n ```{xml_content}```\n\n
#     Convert this BPMN XML into a detailed process description in layman language 
#     without using complex BPMN notations or technical terms
#     and don't add anything by yourself just stay within the context of our BPM:\n```{xml_content}```
#     do styling in response like bold, bullet points headungs etc, 
#     Do not use Markdown formatting (like `*`, `_`, `#`, or triple backticks).
#     Use only valid HTML: <p>, <strong>, <ul>, <li>, <h3>, etc.
#     Wrap everything in a <div> tag at the end.Stay strictly within the BPMN content below:
#     """
    
#     try:
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error in processing BPM to NLD: {str(e)}"

# def generate_query_response(des, query_text):
#     """Sends BPMN XML to Gemini API and gets natural language description."""
#     model = get_gemini_model()
#     prompt = f"""
#     this is  context:\n ```{des}```\n\n 
#     this is query: \n ```{query_text}```\n\n
#     Give Answer to the query from given context (only answer from context do not halucinate or add from yourself), 
#     if query is somehow related to context but answer does not exist in context then say Answer does not found in BPM,
#     if query is to explain the context then do explain,
#     if query is irrelevant to above context say Irrelevant query,
#     do styling in response like bold, bullet points headungs etc, 
#     but in response do not use Markdown formatting (like `*`, `_`, `#`, or triple backticks).
#     Use only valid HTML: <p>, <strong>, <ul>, <li>, <h3>, etc.Wrap everything in a <div> tag at the end.\n"""
    
#     try:
#         response = model.generate_content(prompt)
#         return response.text.strip()
#     except Exception as e:
#         return f"Error in reponsing Query: {str(e)}"



# # import requests

# # RAG_SERVICE_URL = "http://127.0.0.1:8000/rag"  # Adjust based on your setup

# # def convert_bpmn_to_nl(xml_content):
# #     """Call the RAG API to convert BPMN XML to natural language."""
# #     url = f"{RAG_SERVICE_URL}/bpmn-to-nl/"
# #     payload = {"xml_content": xml_content}
    
# #     try:
# #         response = requests.post(url, json=payload)
# #         response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
# #         return response.json().get("nl_description", "Failed to generate description")
# #     except requests.RequestException as e:
# #         print(f"Error in BPMN conversion: {e}")
# #         return "Error converting BPMN to NL"


# # def generate_query_response(query_text):
# #     """Call the RAG API to generate a response using RAG retrieval."""
# #     url = f"{RAG_SERVICE_URL}/query/"
# #     payload = {"query_text": query_text}
    
# #     try:
# #         response = requests.post(url, json=payload)
# #         response.raise_for_status()
# #         return response.json().get("response", "Failed to generate response")
# #     except requests.RequestException as e:
# #         print(f"Error in query response generation: {e}")
# #         return "Error generating query response"
