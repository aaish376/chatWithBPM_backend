import google.generativeai as genai
from django.conf import settings
import os

# Load API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_model():
    # models = genai.list_models()
    # for model in models:
    #     print(model.name)
    print(GEMINI_API_KEY)
    return genai.GenerativeModel("gemini-1.5-pro")


