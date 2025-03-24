import google.generativeai as genai
from django.conf import settings

# Load API key
GEMINI_API_KEY = "AIzaSyDGk3wQUbKZeTBCTfoGEFejFUpkF4RtBf4"
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_model():
    return genai.GenerativeModel("gemini-pro")
