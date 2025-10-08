from ai_client import transcribe_audio, summarize_text

def process_audio(file_path):
    return transcribe_audio(file_path)

def generate_summary(text, max_words=150):
    return summarize_text(text, max_words)
