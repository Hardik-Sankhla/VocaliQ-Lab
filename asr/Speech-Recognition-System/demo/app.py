<<<<<<< HEAD
import tkinter as tk
from tkinter import filedialog, messagebox
import speech_recognition as sr

# Function to process the audio file
def process_audio():
    # Get the file path from the user selection
    file_path = filedialog.askopenfilename(title="Select an Audio File", filetypes=(("WAV Files", "*.wav"), ("All Files", "*.*")))
    
    if file_path:
        recognizer = sr.Recognizer()

        # Open the selected audio file
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)

        # Try to recognize the speech in the audio file
        try:
            text = recognizer.recognize_google(audio)
            result_label.config(text=f"Transcription: {text}")
        except sr.UnknownValueError:
            result_label.config(text="Sorry, I could not understand the audio.")
        except sr.RequestError:
            result_label.config(text="Could not request results from Google Speech Recognition service.")
    else:
        messagebox.showwarning("No File Selected", "Please select an audio file.")

# Setting up the main window
root = tk.Tk()
root.title("Audio Transcription")
root.geometry("400x300")

# UI Components
instruction_label = tk.Label(root, text="Select an audio file to transcribe", font=("Arial", 14))
instruction_label.pack(pady=20)

# Button to select and process audio file
process_button = tk.Button(root, text="Select Audio File", command=process_audio, font=("Arial", 12))
process_button.pack(pady=10)

# Label to display the transcription result
result_label = tk.Label(root, text="Transcription will appear here", font=("Arial", 12), wraplength=350)
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
=======
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

>>>>>>> f86ad24
