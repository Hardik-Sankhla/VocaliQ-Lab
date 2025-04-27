import streamlit as st
import speech_recognition as sr
import tempfile

# Streamlit App
st.set_page_config(page_title="Audio Transcription App", page_icon="🎙️", layout="centered")
st.title("🎙️ Audio Transcription App")
st.write("Upload an audio file and get its transcription!")

# Language selection
language = st.selectbox(
    "Choose language for transcription:",
    ("en-US", "hi-IN", "fr-FR", "es-ES"),
    index=0,
    help="Select the language spoken in the audio."
)

# File uploader
uploaded_file = st.file_uploader("Upload Audio File", type=["wav", "mp3", "flac"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")

    if st.button("Transcribe"):
        with st.spinner('Transcribing... Please wait ⏳'):
            recognizer = sr.Recognizer()

            # Save uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name

            # Load the audio file
            with sr.AudioFile(tmp_file_path) as source:
                audio = recognizer.record(source)

            # Recognize the speech
            try:
                text = recognizer.recognize_google(audio, language=language)
                st.success("Transcription Completed ✅")
                st.text_area("Here’s the Transcribed Text:", text, height=200)

                # Download button
                st.download_button(
                    label="Download Transcription",
                    data=text,
                    file_name="transcription.txt",
                    mime="text/plain"
                )

            except sr.UnknownValueError:
                st.error("Sorry, I could not understand the audio.")
            except sr.RequestError:
                st.error("Could not request results from Google Speech Recognition service.")

else:
    st.info("Please upload an audio file to start.")

