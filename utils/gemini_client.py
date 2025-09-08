import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

def get_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Missing GEMINI_API_KEY in environment variables")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash")