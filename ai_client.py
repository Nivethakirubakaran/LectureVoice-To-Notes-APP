import whisper
import google.generativeai as genai
from config import API_KEY

# Configure Gemini
genai.configure(api_key=API_KEY)

def transcribe_audio(file_path):
    """Transcribe audio using Whisper (runs locally, no billing needed)."""
    model = whisper.load_model("base")  # you can change to "small" or "medium"
    result = model.transcribe(file_path)
    return result["text"]

def summarize_text(text, max_words=150):
    """Summarize text using Gemini."""
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(
        f"Summarize this lecture in about {max_words} words:\n\n{text}"
    )
    return response.text
