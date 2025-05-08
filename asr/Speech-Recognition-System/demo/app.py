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
