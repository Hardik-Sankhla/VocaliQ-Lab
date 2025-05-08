import speech_recognition as sr

def recognize_speech():
    """
    Captures audio from the microphone and transcribes it to text using
    the Google Speech Recognition API.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen with a timeout
            print("Audio captured.")
        except sr.WaitTimeoutError:
            print("No speech detected within the timeout.")
            return None

    try:
        if audio:
            text = recognizer.recognize_google(audio)
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

if __name__ == "__main__":
    recognized_text = recognize_speech()
    if recognized_text:
        print(f"Recognized Text: {recognized_text}")