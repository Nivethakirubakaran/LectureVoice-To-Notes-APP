import streamlit as st
from notes_generator import process_audio, generate_summary

# Page config
st.set_page_config(page_title="Lecture Notes Converter", page_icon="🎓")

# Custom CSS for background and buttons
st.markdown(
    """
    <style>
    body {
        background-color: #f0f8ff;  /* Light blue */
        background-image: url('https://media.giphy.com/media/3o7TKtnuHOHHUjR38Y/giphy.gif');
        background-size: cover;
        background-position: center;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 12px;
        padding: 10px 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("🎉 Turn Your Boring Lectures into Fun Notes! 📝")
st.subheader("Upload your lecture audio and get ready-to-use notes in a snap! ⚡")

# Upload audio file
uploaded_file = st.file_uploader("Upload your lecture audio (MP3/WAV):", type=["mp3", "wav"])

if uploaded_file:
    # Save uploaded file temporarily
    with open("temp_audio", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # User selects summary length
    summary_length = st.selectbox(
        "Select summary length (approximate words):",
        [20, 50, 100, 150]
    )

    # Process audio to transcript
    transcript = process_audio("temp_audio")

    # Generate summary based on user selection
    summary = generate_summary(transcript, summary_length)

    # Display transcript and summary
    st.subheader("📝 Full Transcript")
    st.text_area("Transcript", transcript, height=300)
    st.subheader("🧠 Summary Notes")
    st.text_area("Summary", summary, height=200)

    # Download buttons
    st.download_button("Download Transcript as TXT", transcript, file_name="transcript.txt")
    st.download_button("Download Summary as TXT", summary, file_name="summary.txt")
