import google.generativeai as genai
from django.conf import settings


# Load API key
GEMINI_API_KEY = "AIzaSyDGk3wQUbKZeTBCTfoGEFejFUpkF4RtBf4"
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_model():
    models = genai.list_models()
    for model in models:
        print(model.name)
    return genai.GenerativeModel("gemini-1.5-pro")


