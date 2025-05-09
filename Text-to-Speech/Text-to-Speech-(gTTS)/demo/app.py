import streamlit as st
from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    """
    Convert text to speech and save the output as an audio file.
    :param text: Text to convert to speech
    :param language: Language for speech synthesis (default is English)
    :param output_file: The name of the output audio file
    """
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)
    return output_file

st.title("Text-to-Speech Demo")

text_input = st.text_area("Enter text to convert to speech:", "Hello, welcome to the Text-to-Speech project. I hope you enjoy learning!")

if st.button("Convert to Speech"):
    output_file = text_to_speech(text_input)
    st.audio(output_file, format='audio/mp3')
