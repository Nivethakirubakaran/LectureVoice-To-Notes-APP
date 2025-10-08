import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# List available models
models = genai.list_models()

# Convert generator to list and print each model
for model in models:
    print(model)
