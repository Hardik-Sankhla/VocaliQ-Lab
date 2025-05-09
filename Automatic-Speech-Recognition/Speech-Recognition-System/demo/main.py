import speech_recognition as sr
 
# 1. Initialize the recognizer
recognizer = sr.Recognizer()
 
# 2. Capture the audio from the microphone
with sr.Microphone() as source:
    print("Please say something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source)  # Capture the audio
 
# 3. Recognize the speech using Google Speech Recognition API
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service.")