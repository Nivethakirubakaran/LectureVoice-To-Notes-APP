# 🎙️ Lecture Voice to Notes App

A **Python** app built with **Streamlit** that converts lecture audio into text and summarizes it according to user preference. Users can also download the summarized notes or the raw text for future reference.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-success)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## ✨ Features
- 🎧 Convert lecture audio (live recording or uploaded files) into text  
- 📝 Summarize notes into 20, 50, 100, or 150 words based on user preference  
- 💾 Download summarized notes or the raw text for future reference  
- 🖥️ User-friendly interface built with Streamlit  
- 🎯 Supports multiple audio formats (e.g., mp3, wav, m4a)  
- 🔄 Handles long lecture recordings efficiently  
- 🔍 Allows reviewing and editing the converted text before summarizing  
- ⚡ Fast and responsive processing using Gemini 2.5 Flash for high-quality transcription  
- 🔒 Keeps API keys secure using a `.env` file  

---

## 🚀 Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Nivethakirubakaran/LectureVoice-To-Notes-APP.git
```

2. **Navigate to the project folder:**
```bash
cd LectureVoice-To-Notes-APP
```

3. **Install required Python packages:**
```bash
pip install -r requirements.txt
```

4. **Set up your API key**  
Create a `.env` file in the project folder and add your API key:
```
API_KEY=your_api_key_here
```

---

## 🎯 Usage
Run the app:
```bash
streamlit run app.py
```

- Upload a lecture audio file or record live  
- Choose the summary length  
- View, download, or save the summarized notes  

---

## ⚠️ Notes
- Keep your `.env` file private; do **not** commit it to GitHub  
- Ensure you have a working microphone for live recordings  
- Compatible with Python 3.8+  

---

## 📄 License
This project is licensed under the MIT License. See the `LICENSE` file for details.
