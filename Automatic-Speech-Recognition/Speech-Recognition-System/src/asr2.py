<<<<<<< HEAD
#src/asr.py

import speech_recognition as sr
from .utils import process_audio  # Import the utility function
=======
import speech_recognition as sr
from utils import process_audio  # Absolute import, ensure `utils.py` is in the same directory as `asr2.py`
>>>>>>> f86ad24

def recognize_speech(use_microphone=True, audio_file_path=None):
    """
    Captures audio from the microphone or reads from an audio file and
    transcribes it to text using the Google Speech Recognition API.

    Args:
        use_microphone (bool, optional):  If True, captures audio from the
            microphone.  If False, reads from an audio file.
            Defaults to True.
        audio_file_path (str, optional):  Path to the audio file to read
            if use_microphone is False.  Defaults to None.

    Returns:
        str: The transcribed text, or None on error.
    """
    recognizer = sr.Recognizer()

    if use_microphone:
        with sr.Microphone() as source:
            print("Please say something...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source, timeout=5)
                print("Audio captured from microphone.")
            except sr.WaitTimeoutError:
                print("No speech detected within the timeout.")
                return None
    elif audio_file_path:
<<<<<<< HEAD
        audio_data, samplerate = process_audio(audio_file_path)  # Use the utility
        if audio_data is None:
            return None  # Error already handled in process_audio
        audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)
=======
        audio_data, samplerate = process_audio(audio_file_path)  # Use the utility to process the audio file
        if audio_data is None:
            return None  # Error already handled in process_audio
        audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)  # Convert to AudioData object
>>>>>>> f86ad24
        print(f"Audio read from file: {audio_file_path}")
    else:
        print("Error:  Must specify either use_microphone=True or provide an audio_file_path.")
        return None

    try:
<<<<<<< HEAD
        text = recognizer.recognize_google(audio)
=======
        text = recognizer.recognize_google(audio)  # Recognize using Google's Speech API
>>>>>>> f86ad24
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

<<<<<<< HEAD


if __name__ == "__main__":
    #  Example usage:
    # recognized_text = recognize_speech()  # Use microphone
    recognized_text = recognize_speech(use_microphone=False, audio_file_path="samples/input_audio.wav") # Use file.
    if recognized_text:
        print(f"Recognized Text: {recognized_text}")
=======
# Example usage in the script
if __name__ == "__main__":
    #  Example usage:
    # recognized_text = recognize_speech()  # Use microphone
    recognized_text = recognize_speech(use_microphone=False, audio_file_path=r"F:\VocaliQ-Lab\asr\Speech-Recognition-System\samples\Recording.wav")  # Use audio file
    if recognized_text:
        print(f"Recognized Text: {recognized_text}")
>>>>>>> f86ad24
