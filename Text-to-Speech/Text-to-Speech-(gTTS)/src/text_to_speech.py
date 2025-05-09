from gtts import gTTS
import os

def text_to_speech(text, language='en', output_file='output.mp3'):
    """
    Convert text to speech and save the output as an audio file.
    :param text: Text to convert to speech
    :param language: Language for speech synthesis (default is English)
    :param output_file: The name of the output audio file
    """
    # Initialize gTTS object with text and language
    tts = gTTS(text=text, lang=language, slow=False)  # slow=False makes the speech faster

    # Save the generated speech to an audio file
    tts.save(output_file)
    print(f"Speech saved as {output_file}")

    # Play the generated speech (optional)
    os.system(f"start {output_file}")  # This works on Windows. On macOS use 'afplay', on Linux 'mpg321' or 'aplay'

if __name__ == "__main__":
    # Prompt the user to enter text
    text = input("Enter the text you want to convert to speech: ")
    text_to_speech(text)  # Convert the text to speech and save as 'output.mp3'
