import openai
import os

# Load API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def get_chatgpt_model():
    if not OPENAI_API_KEY:
        raise ValueError("API key not found. Set the OPENAI_API_KEY environment variable.")
    print("API key loaded successfully")
    return openai.ChatCompletion

# import google.generativeai as genai
# from django.conf import settings
# import os

# # Load API key
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# genai.configure(api_key=GEMINI_API_KEY)

# def get_gemini_model():
#     # models = genai.list_models()
#     # for model in models:
#     #     print(model.name)
#     print(GEMINI_API_KEY)
#     return genai.GenerativeModel("gemini-1.5-pro")


